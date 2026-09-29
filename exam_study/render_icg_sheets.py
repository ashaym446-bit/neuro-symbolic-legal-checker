import os
from PIL import Image, ImageDraw, ImageFont

def render_icg_visual(output_path, width=1600, height=950):
    img = Image.new("RGB", (width, height), (15, 23, 42)) # Slate dark theme
    draw = ImageDraw.Draw(img)

    # Fonts
    title_font = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 40)
    sub_font = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 24)
    card_title_font = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 26)
    code_font = ImageFont.truetype("C:/Windows/Fonts/consola.ttf", 20)
    body_font = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 20)

    # Title Banner
    draw.text((60, 40), "INTERMEDIATE-CODE GENERATION: THE 4 INTERMEDIATE LANGUAGES", fill=(255, 255, 255), font=title_font)
    draw.text((60, 95), "Why ICG? Bridges Front-End (Source) and Back-End (Machine). Enables M + N compilers instead of M x N!", fill=(148, 163, 184), font=sub_font)

    # 4 Cards Layout
    cards = [
        {
            "title": "1. SYNTAX TREE (High-Level)",
            "color": (59, 130, 246),
            "desc": "Hierarchical tree where nodes are operators and leaves are operands.",
            "code": ["        [*]", "       /   \\", "     [+]   [+]", "    /  \\   /  \\", "   a    b a    b"]
        },
        {
            "title": "2. DAG (Directed Acyclic Graph)",
            "color": (16, 185, 129),
            "desc": "Eliminates duplicate common subexpressions. Reuses (a + b) node!",
            "code": ["        [*]", "       /   \\", "      +-----+", "     / \\", "    a   b  <-- Shared!"]
        },
        {
            "title": "3. POSTFIX NOTATION (Linear)",
            "color": (245, 158, 11),
            "desc": "Operator comes strictly AFTER its operands. No parentheses needed!",
            "code": ["Expression: (a + b) * c", "", "Postfix Form:", "a b + c *", "(Evaluated using a Stack)"]
        },
        {
            "title": "4. THREE-ADDRESS CODE (Low-Level)",
            "color": (236, 72, 153),
            "desc": "At most 3 addresses (two operands, one result) per instruction.",
            "code": ["t1 = a + b", "t2 = a + b", "t3 = t1 * t2", "x = t3", "(Linearized 3AC sequence)"]
        }
    ]

    card_w = 345
    card_h = 440
    start_x = 60
    start_y = 150
    spacing = 35

    for i, c in enumerate(cards):
        cx = start_x + i * (card_w + spacing)
        cy = start_y

        # Card bg
        draw.rounded_rectangle([cx, cy, cx + card_w, cy + card_h], radius=16, fill=(30, 41, 59), outline=c["color"], width=2)
        
        # Header strip
        draw.rounded_rectangle([cx, cy, cx + card_w, cy + 65], radius=16, fill=c["color"])
        draw.rectangle([cx, cy + 45, cx + card_w, cy + 65], fill=c["color"])
        draw.text((cx + 15, cy + 18), c["title"], fill=(255, 255, 255), font=card_title_font)

        # Desc
        # wrap text
        words = c["desc"].split(" ")
        lines = []
        cur_line = ""
        for w in words:
            if len(cur_line + " " + w) > 28:
                lines.append(cur_line)
                cur_line = w
            else:
                cur_line = (cur_line + " " + w).strip()
        if cur_line:
            lines.append(cur_line)

        dy = cy + 85
        for l in lines:
            draw.text((cx + 20, dy), l, fill=(226, 232, 240), font=body_font)
            dy += 26

        # Code box
        code_box_y = cy + 180
        draw.rounded_rectangle([cx + 15, code_box_y, cx + card_w - 15, cy + card_h - 20], radius=10, fill=(15, 23, 42))
        cdy = code_box_y + 15
        for cl in c["code"]:
            draw.text((cx + 25, cdy), cl, fill=(56, 189, 248), font=code_font)
            cdy += 28

    # Bottom summary bar
    draw.rounded_rectangle([60, 630, width - 60, 890], radius=16, fill=(30, 41, 59), outline=(99, 102, 241), width=2)
    draw.text((90, 655), "CORE EXAM COMPARISON: WHICH ONE TO USE WHEN?", fill=(165, 180, 252), font=card_title_font)
    
    table_rows = [
        "• Syntax Tree: Ideal for front-end parsing and semantic type checking.",
        "• DAG: Essential for compiler optimization (automatically detects common sub-expressions).",
        "• Postfix: Simplest to generate and evaluate via runtime stack-based bytecode (e.g. JVM bytecode).",
        "• Three-Address Code (3AC): Standard industrial representation (bridges high-level syntax with register machine instructions)."
    ]
    ty = 705
    for r in table_rows:
        draw.text((90, ty), r, fill=(241, 245, 249), font=body_font)
        ty += 38

    img.save(output_path, quality=95)
    print(f"Saved Visual: {output_path}")

def render_icg_notes(output_path):
    from render_notes import create_handwritten_notebook
    create_handwritten_notebook(
        output_path=output_path,
        title="INTERMEDIATE-CODE GENERATION (10 MARKS)",
        sections=[
            {
                "heading": "1. Why Generate Intermediate Code? (M x N vs M + N)",
                "highlight": True,
                "content": [
                    "• Retargetability: To build compilers for M source languages and N machines,",
                    "  without IR we need M x N compilers. With IR, we need only M + N components!",
                    "• Machine-Independent Optimization can be applied once on the IR.",
                    "• Front-End = Source to IR; Back-End = IR to Target Machine Code."
                ]
            },
            {
                "heading": "2. Major Forms of Intermediate Languages",
                "highlight": False,
                "content": [
                    "1. Postfix Notation: Operator follows operands. Example: a b + c *",
                    "2. Syntax Tree: Tree representation of the parsed grammar.",
                    "3. Directed Acyclic Graph (DAG): Syntax tree that compresses identical sub-trees.",
                    "4. Three-Address Code (3AC): Sequence of instructions with at most 3 addresses."
                ]
            },
            {
                "heading": "3. Three-Address Code (3AC) General Format",
                "highlight": True,
                "content": [
                    "General Form: x = y op z  (where x is result, y & z are operands, op is operator).",
                    "Only ONE operator allowed on the right-hand side!",
                    "Example: Convert x = a + b * c into 3AC:",
                    "  t1 = b * c",
                    "  t2 = a + t1",
                    "  x = t2"
                ]
            },
            {
                "heading": "4. Common 3AC Statement Types (Must List in Exam)",
                "highlight": False,
                "content": [
                    "• Assignment: x = y op z  OR  x = op y",
                    "• Copy statement: x = y",
                    "• Unconditional Jump: goto L",
                    "• Conditional Jump: if x relop y goto L",
                    "• Procedure Call: param x; call p, n; return y"
                ]
            }
        ],
        exam_tip="Always write the M + N benefit diagram and show the 3AC conversion for x = a + b * c\nto secure full 10 marks!"
    )

if __name__ == "__main__":
    visual_path = "f:/kachara/project final year/exam_study/compiler_design/cd_m4_icg_languages_visual.jpg"
    notes_path = "f:/kachara/project final year/exam_study/compiler_design/cd_m4_icg_languages_notes.jpg"
    render_icg_visual(visual_path)
    render_icg_notes(notes_path)
