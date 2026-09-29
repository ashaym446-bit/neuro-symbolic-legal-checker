import os
from PIL import Image, ImageDraw, ImageFont

def render_declarations_visual(output_path, width=1600, height=980):
    img = Image.new("RGB", (width, height), (15, 23, 42))
    draw = ImageDraw.Draw(img)

    title_font = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 36)
    sub_font = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 22)
    card_title_font = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 24)
    data_font = ImageFont.truetype("C:/Windows/Fonts/consola.ttf", 19)
    body_font = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 19)

    # Header
    draw.text((60, 30), "DECLARATIONS & STORAGE LAYOUT: HOW COMPILERS ASSIGN MEMORY OFFSETS", fill=(255, 255, 255), font=title_font)
    draw.text((60, 78), "Goal: Calculate relative address (offset) for each declared variable and store in Symbol Table.", fill=(56, 189, 248), font=sub_font)

    # 1. Left Card: Syntax-Directed Definition (Grammar & Rules)
    cx1 = 60
    cy1 = 130
    cw1 = 700
    ch1 = 570
    draw.rounded_rectangle([cx1, cy1, cx1 + cw1, cy1 + ch1], radius=14, fill=(30, 41, 59), outline=(59, 130, 246), width=2)
    draw.rounded_rectangle([cx1, cy1, cx1 + cw1, cy1 + 60], radius=14, fill=(59, 130, 246))
    draw.rectangle([cx1, cy1 + 40, cx1 + cw1, cy1 + 60], fill=(59, 130, 246))
    draw.text((cx1 + 20, cy1 + 15), "1. SDD RULES FOR TYPE DECLARATIONS", fill=(255, 255, 255), font=card_title_font)

    sdd_lines = [
        ("P -> { offset = 0 } D", "Initialize global offset counter to 0"),
        ("D -> D ; D", "Sequence of declarations"),
        ("D -> id : T", "{ enter(id.name, T.type, offset);"),
        (" ", "  offset = offset + T.width }"),
        ("T -> integer", "{ T.type = integer; T.width = 4; }"),
        ("T -> float", "{ T.type = float; T.width = 8; }"),
        ("T -> char", "{ T.type = char; T.width = 1; }"),
        ("T -> array [ num ] of T1", "{ T.type = array(num.val, T1.type);"),
        (" ", "  T.width = num.val * T1.width }"),
        ("T -> ^ T1", "{ T.type = pointer(T1.type); T.width = 4; }")
    ]
    dy = cy1 + 80
    for prod, meaning in sdd_lines:
        draw.text((cx1 + 25, dy), prod, fill=(250, 204, 21), font=data_font)
        if meaning:
            draw.text((cx1 + 330, dy), "// " + meaning, fill=(148, 163, 184), font=body_font)
        dy += 44

    # 2. Right Card: Memory Layout Tape & Symbol Table
    cx2 = 790
    cy2 = 130
    cw2 = 750
    ch2 = 570
    draw.rounded_rectangle([cx2, cy2, cx2 + cw2, cy2 + ch2], radius=14, fill=(30, 41, 59), outline=(16, 185, 129), width=2)
    draw.rounded_rectangle([cx2, cy2, cx2 + cw2, cy2 + 60], radius=14, fill=(16, 185, 129))
    draw.rectangle([cx2, cy2 + 40, cx2 + cw2, cy2 + 60], fill=(16, 185, 129))
    draw.text((cx2 + 20, cy2 + 15), "2. TRACE: x : int; y : float; A : array[10] of int;", fill=(255, 255, 255), font=card_title_font)

    # Memory Layout Visualization (Blocks)
    draw.text((cx2 + 25, cy2 + 80), "RELATIVE MEMORY OFFSETS IN ACTIVATION RECORD:", fill=(165, 180, 252), font=card_title_font)
    
    # Blocks
    # Block 1: x (0..4)
    draw.rectangle([cx2 + 25, cy2 + 120, cx2 + 175, cy2 + 190], fill=(59, 130, 246), outline=(255, 255, 255), width=2)
    draw.text((cx2 + 55, cy2 + 135), "x (int)", fill=(255, 255, 255), font=data_font)
    draw.text((cx2 + 50, cy2 + 160), "4 bytes", fill=(226, 232, 240), font=body_font)
    draw.text((cx2 + 25, cy2 + 195), "Offset: 0", fill=(250, 204, 21), font=data_font)

    # Block 2: y (4..12)
    draw.rectangle([cx2 + 185, cy2 + 120, cx2 + 375, cy2 + 190], fill=(236, 72, 153), outline=(255, 255, 255), width=2)
    draw.text((cx2 + 240, cy2 + 135), "y (float)", fill=(255, 255, 255), font=data_font)
    draw.text((cx2 + 245, cy2 + 160), "8 bytes", fill=(226, 232, 240), font=body_font)
    draw.text((cx2 + 185, cy2 + 195), "Offset: 4", fill=(250, 204, 21), font=data_font)

    # Block 3: A (12..52)
    draw.rectangle([cx2 + 385, cy2 + 120, cx2 + 710, cy2 + 190], fill=(16, 185, 129), outline=(255, 255, 255), width=2)
    draw.text((cx2 + 470, cy2 + 135), "A (array[10] of int)", fill=(255, 255, 255), font=data_font)
    draw.text((cx2 + 480, cy2 + 160), "10 x 4 = 40 bytes", fill=(226, 232, 240), font=body_font)
    draw.text((cx2 + 385, cy2 + 195), "Offset: 12", fill=(250, 204, 21), font=data_font)
    draw.text((cx2 + 640, cy2 + 195), "Total: 52", fill=(248, 113, 113), font=data_font)

    # Symbol Table Box
    draw.text((cx2 + 25, cy2 + 250), "RESULTING SYMBOL TABLE ENTRIES:", fill=(165, 180, 252), font=card_title_font)
    
    headers = ["Name", "Type", "Width (bytes)", "Relative Offset"]
    st_widths = [120, 240, 150, 160]
    st_y = cy2 + 290
    st_x = cx2 + 25
    for idx, h in enumerate(headers):
        draw.text((st_x, st_y), h, fill=(255, 255, 255), font=card_title_font)
        st_x += st_widths[idx]
    
    draw.line([(cx2 + 25, st_y + 35), (cx2 + cw2 - 25, st_y + 35)], fill=(100, 116, 139), width=2)
    
    st_rows = [
        ["x", "integer", "4", "0"],
        ["y", "float", "8", "4"],
        ["A", "array(10, integer)", "40", "12"]
    ]
    r_y = st_y + 50
    for row in st_rows:
        rx = cx2 + 25
        for idx, cell in enumerate(row):
            draw.text((rx, r_y), cell, fill=(56, 189, 248) if idx == 0 or idx == 3 else (226, 232, 240), font=data_font)
            rx += st_widths[idx]
        r_y += 42

    # Bottom Exam Tip Bar
    draw.rounded_rectangle([60, 725, width - 60, 930], radius=14, fill=(30, 41, 59), outline=(245, 158, 11), width=2)
    draw.text((90, 745), "★ EXAM SUMMARY: 3 STEPS TO SOLVE ANY DECLARATION NUMERICAL", fill=(254, 240, 138), font=card_title_font)
    draw.text((90, 790), "1. Set offset = 0 initially.", fill=(255, 255, 255), font=data_font)
    draw.text((90, 830), "2. For each variable: SymbolTable.enter(name, type, current_offset).", fill=(255, 255, 255), font=data_font)
    draw.text((90, 870), "3. Advance offset: offset = offset + width (Remember: array width = num_elements * element_width).", fill=(255, 255, 255), font=data_font)

    img.save(output_path, quality=95)
    print(f"Saved Visual: {output_path}")

def render_declarations_notes(output_path):
    from render_notes import create_handwritten_notebook
    create_handwritten_notebook(
        output_path=output_path,
        title="DECLARATIONS & STORAGE LAYOUT (10 MARKS)",
        sections=[
            {
                "heading": "1. What is Storage Layout in Declarations?",
                "highlight": True,
                "content": [
                    "During declarations, the compiler determines the relative address (offset)",
                    "for each identifier within the procedure's activation record.",
                    "Offset calculation is performed using Syntax-Directed Translation (SDT)."
                ]
            },
            {
                "heading": "2. Syntax-Directed Definition (SDD) for Types",
                "highlight": False,
                "content": [
                    "• P -> { offset = 0; } D",
                    "• D -> id : T  { enter(id.name, T.type, offset); offset = offset + T.width; }",
                    "• T -> int  { T.type = integer; T.width = 4; }",
                    "• T -> float  { T.type = float; T.width = 8; }",
                    "• T -> array [ num ] of T1  { T.type = array(num.val, T1.type);",
                    "                              T.width = num.val * T1.width; }"
                ]
            },
            {
                "heading": "3. Solved Exam Numerical",
                "highlight": True,
                "content": [
                    "Given declarations:  x : int;  y : float;  A : array[10] of int;",
                    "1. Initially: offset = 0",
                    "2. id 'x' (int): enter('x', int, 0) -> offset = 0 + 4 = 4",
                    "3. id 'y' (float): enter('y', float, 4) -> offset = 4 + 8 = 12",
                    "4. id 'A' (array[10] of int): width = 10 * 4 = 40",
                    "   enter('A', array(10, int), 12) -> offset = 12 + 40 = 52."
                ]
            },
            {
                "heading": "4. Key Function: enter(name, type, offset)",
                "highlight": False,
                "content": [
                    "• Installs variable symbol table entry with its type and offset.",
                    "• Used later during code generation to emit assembly: e.g. MOV 4(FP), R0."
                ]
            }
        ],
        exam_tip="Always show the recursive width calculation for arrays: width = num * width(T1).\nDraw the Symbol Table columns: Name | Type | Width | Offset for full marks!"
    )

if __name__ == "__main__":
    visual_path = "f:/kachara/project final year/exam_study/compiler_design/cd_m4_declarations_visual.jpg"
    notes_path = "f:/kachara/project final year/exam_study/compiler_design/cd_m4_declarations_notes.jpg"
    render_declarations_visual(visual_path)
    render_declarations_notes(notes_path)
