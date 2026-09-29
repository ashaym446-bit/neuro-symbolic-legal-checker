import os
from PIL import Image, ImageDraw, ImageFont

def render_3ac_visual(output_path, width=1600, height=1000):
    img = Image.new("RGB", (width, height), (15, 23, 42))
    draw = ImageDraw.Draw(img)

    title_font = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 36)
    sub_font = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 22)
    col_hdr_font = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 20)
    data_font = ImageFont.truetype("C:/Windows/Fonts/consola.ttf", 19)
    card_title_font = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 24)

    # Header
    draw.text((60, 30), "REPRESENTATIONS OF THREE-ADDRESS CODE: QUADRUPLES vs TRIPLES vs INDIRECT TRIPLES", fill=(255, 255, 255), font=title_font)
    draw.text((60, 78), "Sample Expression to convert:  x = (a + b) * -c", fill=(56, 189, 248), font=sub_font)
    draw.text((60, 110), "3AC:  (0) t1 = a + b    (1) t2 = uminus c    (2) t3 = t1 * t2    (3) x = t3", fill=(148, 163, 184), font=data_font)

    # 3 Column Tables Layout
    tables = [
        {
            "title": "1. QUADRUPLES (4 Fields)",
            "subtitle": "Fields: (op, arg1, arg2, result)",
            "color": (59, 130, 246),
            "headers": ["Index", "op", "arg1", "arg2", "result"],
            "col_widths": [65, 80, 80, 80, 90],
            "rows": [
                ["(0)", "+", "a", "b", "t1"],
                ["(1)", "uminus", "c", "-", "t2"],
                ["(2)", "*", "t1", "t2", "t3"],
                ["(3)", "=", "t3", "-", "x"]
            ],
            "pro": "Easy to reorder instructions for optimization.",
            "con": "Wastes memory storing explicit temporary names."
        },
        {
            "title": "2. TRIPLES (3 Fields)",
            "subtitle": "Fields: (op, arg1, arg2)",
            "color": (16, 185, 129),
            "headers": ["Index", "op", "arg1", "arg2"],
            "col_widths": [70, 95, 115, 115],
            "rows": [
                ["(0)", "+", "a", "b"],
                ["(1)", "uminus", "c", "-"],
                ["(2)", "*", "(0)", "(1)"],
                ["(3)", "=", "x", "(2)"]
            ],
            "pro": "Saves memory: uses pointers (0),(1) instead of t1,t2.",
            "con": "Hard to optimize! Moving code changes pointer indices."
        },
        {
            "title": "3. INDIRECT TRIPLES",
            "subtitle": "Array of Pointers + Triples Table",
            "color": (245, 158, 11),
            "headers": ["StmtPtr", "Points To", "Triples Table"],
            "col_widths": [90, 105, 195],
            "rows": [
                ["p[0] ->", "(0)", "(+) a, b"],
                ["p[1] ->", "(1)", "(uminus) c, -"],
                ["p[2] ->", "(2)", "(*) (0), (1)"],
                ["p[3] ->", "(3)", "(=) x, (2)"]
            ],
            "pro": "Best of both: Saves memory AND allows easy reordering",
            "con": "just by moving the pointer array entries!"
        }
    ]

    card_w = 460
    card_h = 560
    start_x = 60
    start_y = 160
    spacing = 40

    for i, t in enumerate(tables):
        cx = start_x + i * (card_w + spacing)
        cy = start_y

        draw.rounded_rectangle([cx, cy, cx + card_w, cy + card_h], radius=14, fill=(30, 41, 59), outline=t["color"], width=2)
        draw.rounded_rectangle([cx, cy, cx + card_w, cy + 65], radius=14, fill=t["color"])
        draw.rectangle([cx, cy + 45, cx + card_w, cy + 65], fill=t["color"])

        draw.text((cx + 15, cy + 12), t["title"], fill=(255, 255, 255), font=card_title_font)
        draw.text((cx + 15, cy + 40), t["subtitle"], fill=(254, 240, 138), font=data_font)

        # Table Header
        ty = cy + 85
        tx = cx + 15
        for h_idx, h in enumerate(t["headers"]):
            draw.text((tx, ty), h, fill=(241, 245, 249), font=col_hdr_font)
            tx += t["col_widths"][h_idx]
        
        draw.line([(cx + 15, ty + 30), (cx + card_w - 15, ty + 30)], fill=(100, 116, 139), width=2)

        # Table Rows
        ry = ty + 42
        for row in t["rows"]:
            rx = cx + 15
            for c_idx, cell in enumerate(row):
                draw.text((rx, ry), cell, fill=(56, 189, 248) if "(" in cell or "t" in cell else (255, 255, 255), font=data_font)
                rx += t["col_widths"][c_idx]
            ry += 38

        # Pros/Cons
        draw.line([(cx + 15, cy + card_h - 130), (cx + card_w - 15, cy + card_h - 130)], fill=(71, 85, 105), width=1)
        draw.text((cx + 15, cy + card_h - 115), "✓ Pro: " + t["pro"][:42], fill=(74, 222, 128), font=data_font)
        draw.text((cx + 15, cy + card_h - 85), "   " + t["pro"][42:], fill=(74, 222, 128), font=data_font)
        draw.text((cx + 15, cy + card_h - 55), "✗ Con: " + t["con"], fill=(248, 113, 113), font=data_font)

    # Bottom summary
    draw.rounded_rectangle([60, 755, width - 60, 960], radius=14, fill=(30, 41, 59), outline=(147, 51, 234), width=2)
    draw.text((90, 775), "⚡ 10-MARK EXAM CHEAT-SHEET FOR SOLVING NUMERICALS", fill=(216, 180, 254), font=card_title_font)
    draw.text((90, 820), "Step 1: Always break the expression into 3AC first with only 1 operator per line.", fill=(255, 255, 255), font=data_font)
    draw.text((90, 860), "Step 2: For Quadruples, fill: op | arg1 | arg2 | result (using temporary variables t1, t2...).", fill=(255, 255, 255), font=data_font)
    draw.text((90, 900), "Step 3: For Triples, drop the 'result' column! Put instruction pointers like (0), (1) inside arg1 or arg2.", fill=(255, 255, 255), font=data_font)

    img.save(output_path, quality=95)
    print(f"Saved Visual: {output_path}")

def render_3ac_notes(output_path):
    from render_notes import create_handwritten_notebook
    create_handwritten_notebook(
        output_path=output_path,
        title="QUADRUPLES, TRIPLES & INDIRECT TRIPLES (10M)",
        sections=[
            {
                "heading": "1. What are 3AC Representations?",
                "highlight": True,
                "content": [
                    "3AC instructions must be stored in data structures inside the compiler.",
                    "Three primary representations: Quadruples, Triples, and Indirect Triples."
                ]
            },
            {
                "heading": "2. Quadruples: Record with 4 fields (op, arg1, arg2, result)",
                "highlight": False,
                "content": [
                    "• Example: t1 = a + b becomes (+, a, b, t1).",
                    "• Advantage: Instructions can be moved around freely without changing references.",
                    "• Disadvantage: Creates tons of temporary variables, inflating the symbol table."
                ]
            },
            {
                "heading": "3. Triples: Record with 3 fields (op, arg1, arg2)",
                "highlight": True,
                "content": [
                    "• Avoids explicit temporary variables! References previous results by position: (0), (1).",
                    "• Example: (0) (+, a, b)  and  (1) (*, (0), c)  meaning (a + b) * c.",
                    "• Disadvantage: Very difficult to optimize. If you move statement (0), all pointers break!"
                ]
            },
            {
                "heading": "4. Indirect Triples: Array of Pointers to Triples",
                "highlight": False,
                "content": [
                    "• Stores triples in one table, and has a separate array of pointers p[0], p[1]...",
                    "• To reorder code during optimization, just swap entries in the pointer array!",
                    "• The underlying triples remain untouched. Best of both worlds!"
                ]
            }
        ],
        exam_tip="Exam numerical question: Convert x = (a + b) * -c into all 3 representations.\nAlways draw the 3 tables neatly with clear headers for full 10 marks!"
    )

if __name__ == "__main__":
    visual_path = "f:/kachara/project final year/exam_study/compiler_design/cd_m4_3ac_representations_visual.jpg"
    notes_path = "f:/kachara/project final year/exam_study/compiler_design/cd_m4_3ac_representations_notes.jpg"
    render_3ac_visual(visual_path)
    render_3ac_notes(notes_path)
