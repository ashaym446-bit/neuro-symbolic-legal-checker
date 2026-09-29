import os
from PIL import Image, ImageDraw, ImageFont

def render_nn_hessian_visual(output_path, width=1600, height=1000):
    img = Image.new("RGB", (width, height), (15, 23, 42))
    draw = ImageDraw.Draw(img)

    title_font = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 36)
    sub_font = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 22)
    card_title_font = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 24)
    data_font = ImageFont.truetype("C:/Windows/Fonts/consola.ttf", 19)
    body_font = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 19)

    # Header
    draw.text((60, 30), "NEURAL NETWORKS: THE HESSIAN MATRIX & ERROR SURFACE CURVATURE", fill=(255, 255, 255), font=title_font)
    draw.text((60, 78), "Syllabus Topic: 2nd-Order Optimization in Backpropagation. What is the Hessian & why do we need it?", fill=(56, 189, 248), font=sub_font)

    # 3 Cards Layout
    card_w = 460
    card_h = 580
    start_x = 60
    start_y = 130
    spacing = 40

    cards = [
        {
            "title": "1. 1ST VS 2ND DERIVATIVE",
            "subtitle": "Gradient (Slope) vs Hessian (Curvature)",
            "color": (59, 130, 246),
            "lines": [
                ("Gradient (g = dE/dw):", "Tells you the DIRECTION of steepest slope."),
                ("Hessian (H = d^2E/dw^2):", "Tells you the CURVATURE (how curved/flat the bowl is)."),
                ("", ""),
                ("Analogy:", "Driving in a fog:"),
                ("• Gradient:", "Tells you if the road goes up or down."),
                ("• Hessian:", "Tells you if a sharp bend or steep cliff is ahead!")
            ]
        },
        {
            "title": "2. THE ILL-CONDITIONED CANYON",
            "subtitle": "Why Standard Gradient Descent Fails",
            "color": (239, 68, 68),
            "lines": [
                ("The Problem:", "Error surfaces are usually elongated ravines (steep walls, flat valley floor)."),
                ("", ""),
                ("Standard Gradient Descent:", "Oscillates wildly back & forth across steep walls, making agonizingly slow progress down the valley!"),
                ("", ""),
                ("Newton's Method (using H^-1):", "Scales steps by curvature: takes small steps across steep walls, huge steps along flat valley floor straight to the minimum!")
            ]
        },
        {
            "title": "3. THE PRACTICAL BOTTLENECK",
            "subtitle": "Why Can't We Always Invert H?",
            "color": (245, 158, 11),
            "lines": [
                ("Matrix Size:", "If network has N weights, Hessian is N x N."),
                ("Example:", "For 100,000 weights -> 10 BILLION entries!"),
                ("", ""),
                ("Inversion Cost O(N^3):", "Inverting H^-1 is computationally impossible for deep neural networks."),
                ("", ""),
                ("Modern Solutions:", "• Levenberg-Marquardt (small nets)"),
                ("• Quasi-Newton (L-BFGS)", "• Momentum & Adam (approximate)")
            ]
        }
    ]

    for i, c in enumerate(cards):
        cx = start_x + i * (card_w + spacing)
        cy = start_y

        draw.rounded_rectangle([cx, cy, cx + card_w, cy + card_h], radius=14, fill=(30, 41, 59), outline=c["color"], width=2)
        draw.rounded_rectangle([cx, cy, cx + card_w, cy + 65], radius=14, fill=c["color"])
        draw.rectangle([cx, cy + 45, cx + card_w, cy + 65], fill=c["color"])

        draw.text((cx + 15, cy + 12), c["title"], fill=(255, 255, 255), font=card_title_font)
        draw.text((cx + 15, cy + 40), c["subtitle"], fill=(254, 240, 138), font=data_font)

        dy = cy + 85
        for lbl, val in c["lines"]:
            if lbl:
                draw.text((cx + 20, dy), lbl, fill=(56, 189, 248), font=card_title_font)
                dy += 28
            if val:
                # word wrap
                words = val.split(" ")
                cur = ""
                for w in words:
                    if len(cur + " " + w) > 34:
                        draw.text((cx + 20, dy), cur, fill=(226, 232, 240), font=body_font)
                        dy += 24
                        cur = w
                    else:
                        cur = (cur + " " + w).strip()
                if cur:
                    draw.text((cx + 20, dy), cur, fill=(226, 232, 240), font=body_font)
                    dy += 26
            dy += 6

    # Bottom Formula Card
    draw.rounded_rectangle([60, 740, width - 60, 960], radius=14, fill=(30, 41, 59), outline=(16, 185, 129), width=2)
    draw.text((90, 755), "★ EXAM CORE FORMULAS: TAYLOR SERIES EXPANSION & NEWTON UPDATE", fill=(110, 231, 183), font=card_title_font)
    draw.text((90, 800), "Taylor Series: E(w + dw) ≈ E(w) + g^T * dw + 0.5 * dw^T * H * dw", fill=(250, 204, 21), font=data_font)
    draw.text((90, 840), "Hessian Matrix: H_ij = [ d^2 E / (dw_i * dw_j) ]   (Symmetric square matrix of size N x N)", fill=(255, 255, 255), font=data_font)
    draw.text((90, 880), "Optimal Newton Step: dw = - H^-1 * g   (Jumps directly to the quadratic minimum in ONE step!)", fill=(56, 189, 248), font=data_font)
    draw.text((90, 920), "Eigenvalues of H: Positive definite (all λ > 0) = Minimum; Indefinite (mixed signs) = Saddle Point.", fill=(248, 113, 113), font=data_font)

    img.save(output_path, quality=95)
    print(f"Saved Visual: {output_path}")

def render_nn_hessian_notes(output_path):
    from render_notes import create_handwritten_notebook
    create_handwritten_notebook(
        output_path=output_path,
        title="HESSIAN MATRIX IN NEURAL NETWORKS (10 MARKS)",
        sections=[
            {
                "heading": "1. Definition & Formula of Hessian Matrix",
                "highlight": True,
                "content": [
                    "• The Hessian H is a square matrix of second-order partial derivatives of Error E",
                    "  with respect to weight parameters: H_ij = d^2 E / (dw_i dw_j).",
                    "• Size: N x N (where N is total number of tunable weights in network).",
                    "• Property: Symmetric matrix (H_ij = H_ji by Clairaut's theorem)."
                ]
            },
            {
                "heading": "2. Geometric Role: Error Surface Curvature",
                "highlight": False,
                "content": [
                    "• 1st Derivative (Gradient g): Specifies the direction of steepest slope.",
                    "• 2nd Derivative (Hessian H): Specifies the curvature (rate of slope change).",
                    "• Eigenvalues of H (lambda):",
                    "  - All lambda > 0: Local Minimum (bowl shape).",
                    "  - All lambda < 0: Local Maximum (dome shape).",
                    "  - Mixed signs: Saddle point (inflection point)."
                ]
            },
            {
                "heading": "3. Newton's Weight Update Formula",
                "highlight": True,
                "content": [
                    "• Quadratic Taylor Series: E(w + dw) = E(w) + g^T dw + 0.5 dw^T H dw.",
                    "• Differentiating w.r.t dw and equating to 0 yields:",
                    "  Delta w = - H^-1 * g",
                    "• Key Benefit: Converges quadratically (much faster than gradient descent)."
                ]
            },
            {
                "heading": "4. Why is Hessian Impractical for Deep Networks?",
                "highlight": False,
                "content": [
                    "• Memory: Storing N x N matrix requires O(N^2) space (GigaBytes for deep nets).",
                    "• Computation: Inverting H requires O(N^3) time operations.",
                    "• Popular Approximations: Levenberg-Marquardt (LM), Gauss-Newton, BFGS."
                ]
            }
        ],
        exam_tip="Write the Taylor expansion, H_ij formula, and Newton's delta w = -H^-1 * g.\nMention the O(N^3) inversion bottleneck to get full 10 marks!"
    )

if __name__ == "__main__":
    visual_path = "f:/kachara/project final year/exam_study/neural_networks/nn_m4_hessian_visual.jpg"
    notes_path = "f:/kachara/project final year/exam_study/neural_networks/nn_m4_hessian_notes.jpg"
    render_nn_hessian_visual(visual_path)
    render_nn_hessian_notes(notes_path)
