import os
from PIL import Image, ImageDraw, ImageFont

def create_handwritten_notebook(
    output_path,
    title,
    sections,
    exam_tip=None,
    width=1400,
    height=1900
):
    # 1. Create paper background (slightly warm cream white)
    img = Image.new("RGB", (width, height), (252, 252, 250))
    draw = ImageDraw.Draw(img)

    # 2. Draw ruled blue lines
    line_spacing = 42
    start_y = 180
    margin_x = 160

    # Vertical Red Margin
    draw.line([(margin_x, 0), (margin_x, height)], fill=(235, 120, 120), width=3)
    draw.line([(margin_x + 4, 0), (margin_x + 4, height)], fill=(245, 160, 160), width=1)

    # Horizontal Ruled Lines
    for y in range(start_y, height - 80, line_spacing):
        draw.line([(0, y), (width, y)], fill=(215, 228, 245), width=2)

    # Fonts
    font_path = "C:/Windows/Fonts/Inkfree.ttf"
    if not os.path.exists(font_path):
        font_path = "C:/Windows/Fonts/comic.ttf"

    title_font = ImageFont.truetype(font_path, 42)
    header_font = ImageFont.truetype(font_path, 34)
    body_font = ImageFont.truetype(font_path, 28)
    tip_font = ImageFont.truetype(font_path, 26)

    # 3. Write Title
    title_box = draw.textbbox((margin_x + 30, 80), title, font=title_font)
    # Underline title
    draw.text((margin_x + 30, 80), title, fill=(20, 35, 110), font=title_font)
    draw.line([(margin_x + 30, title_box[3] + 4), (title_box[2] + 40, title_box[3] + 4)], fill=(180, 40, 40), width=3)

    cur_y = 205
    text_x = margin_x + 30

    for sec in sections:
        # Check highlighter
        if sec.get("highlight"):
            h_text = sec["heading"]
            bbox = draw.textbbox((text_x, cur_y), h_text, font=header_font)
            # Yellow highlighter rect
            draw.rectangle([bbox[0]-6, bbox[1]-4, bbox[2]+8, bbox[3]+4], fill=(255, 245, 130))
            draw.text((text_x, cur_y), h_text, fill=(15, 25, 90), font=header_font)
        else:
            draw.text((text_x, cur_y), sec["heading"], fill=(160, 20, 20), font=header_font)
        
        cur_y += line_spacing

        for line in sec.get("content", []):
            if isinstance(line, tuple):
                # (label, text)
                draw.text((text_x + 20, cur_y), f"• {line[0]}: ", fill=(10, 20, 100), font=body_font)
                l_box = draw.textbbox((text_x + 20, cur_y), f"• {line[0]}: ", font=body_font)
                draw.text((l_box[2] + 5, cur_y), line[1], fill=(40, 40, 45), font=body_font)
            else:
                draw.text((text_x + 20, cur_y), line, fill=(25, 30, 80), font=body_font)
            cur_y += line_spacing
        
        cur_y += 15

    # 4. Exam Tip Box at bottom
    if exam_tip:
        box_y1 = height - 230
        box_y2 = height - 90
        draw.rectangle([margin_x + 20, box_y1, width - 80, box_y2], fill=(255, 250, 210), outline=(200, 50, 50), width=3)
        draw.text((margin_x + 40, box_y1 + 15), "★ EXAM TIP (High-Yield):", fill=(190, 25, 25), font=header_font)
        draw.text((margin_x + 40, box_y1 + 60), exam_tip, fill=(20, 30, 90), font=tip_font)

    # Save
    img.save(output_path, quality=95)
    print(f"Saved: {output_path}")

if __name__ == "__main__":
    create_handwritten_notebook(
        output_path="f:/kachara/project final year/exam_study/compiler_design/cd_m4_equiv_notes.jpg",
        title="EQUIVALENCE OF TYPE EXPRESSIONS (5-10 MARKS)",
        sections=[
            {
                "heading": "1. What is Type Equivalence?",
                "highlight": True,
                "content": [
                    "A type checker needs to decide if type s and type t are identical.",
                    "Two main approaches: Name Equivalence vs Structural Equivalence."
                ]
            },
            {
                "heading": "2. Name Equivalence (Strict)",
                "highlight": False,
                "content": [
                    "Rule: Two type expressions are equal iff they have the exact same name.",
                    "Example: typedef int Length; typedef int Width;",
                    "Under Name Equivalence: Length != Width (Assignment ERROR!).",
                    "Advantage: Very fast check, enforces semantic domain safety.",
                    "Disadvantage: Too strict for many general operations."
                ]
            },
            {
                "heading": "3. Structural Equivalence (Flexible)",
                "highlight": True,
                "content": [
                    "Rule: Two types are equal iff they have the exact same internal structure.",
                    "Recursive Definition:",
                    "  • Basic types are equivalent only if identical (int == int).",
                    "  • array(s1, t1) == array(s2, t2) iff s1 == s2 and t1 == t2.",
                    "  • pointer(t1) == pointer(t2) iff t1 == t2.",
                    "  • s1 -> t1 == s2 -> t2 iff s1 == s2 and t1 == t2."
                ]
            },
            {
                "heading": "4. Comparison Table (Must Draw in Exam!)",
                "highlight": False,
                "content": [
                    "• Check Basis: Type Name Only vs Internal Structure Skeleton",
                    "• Complexity: O(1) string/symbol compare vs Recursive Tree Traversal",
                    "• Cyclic Types: No issue vs Requires Cycle-Detection (Visited Graph)",
                    "• Used In: Pascal, Ada (Strict) vs C, Algol-68 (Structural)"
                ]
            }
        ],
        exam_tip="If asked to compare (5M), ALWAYS write the recursive definition rules for array/pointer\nand mention the cyclic graph problem (e.g., struct Node { struct Node *next; })."
    )
