import os
from PIL import Image, ImageDraw, ImageFont

def render_pruning_visual(output_path, width=1600, height=1000):
    img = Image.new("RGB", (width, height), (15, 23, 42))
    draw = ImageDraw.Draw(img)

    title_font = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 36)
    sub_font = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 22)
    card_title_font = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 24)
    data_font = ImageFont.truetype("C:/Windows/Fonts/consola.ttf", 19)
    body_font = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 19)

    # Header
    draw.text((60, 30), "NEURAL NETWORKS: GENERALIZATION, CROSS-VALIDATION & NETWORK PRUNING", fill=(255, 255, 255), font=title_font)
    draw.text((60, 78), "How do we make networks perform accurately on unseen real-world data and remove redundant weights?", fill=(56, 189, 248), font=sub_font)

    # 3 Cards Layout
    card_w = 460
    card_h = 580
    start_x = 60
    start_y = 130
    spacing = 40

    cards = [
        {
            "title": "1. WHAT IS GENERALIZATION?",
            "subtitle": "Underfitting vs Overfitting",
            "color": (59, 130, 246),
            "lines": [
                ("Generalization:", "Ability to predict accurately on UNSEEN test samples."),
                ("", ""),
                ("• Underfitting (High Bias):", "Model is too simple (e.g. straight line for complex curve). High train & test error."),
                ("", ""),
                ("• Overfitting (High Variance):", "Network has too many parameters. Memorizes training noise! Zero train error, terrible test error!"),
                ("", ""),
                ("• Occam's Razor:", "The simplest network architecture that fits data generalizes best.")
            ]
        },
        {
            "title": "2. K-FOLD CROSS-VALIDATION",
            "subtitle": "Unbiased Performance Evaluation",
            "color": (16, 185, 129),
            "lines": [
                ("How it works:", "Split entire dataset into K equal folds (e.g. K=5)."),
                ("", ""),
                ("In each iteration:", "• Train on K - 1 folds."),
                ("", "• Test on the remaining 1 held-out fold."),
                ("", ""),
                ("Final Score:", "Average error across all K folds."),
                ("", ""),
                ("Key Benefit:", "Every single sample gets used for both training & testing. Prevents selection bias!")
            ]
        },
        {
            "title": "3. NETWORK PRUNING TECHNIQUES",
            "subtitle": "Optimal Brain Damage (OBD) & OBS",
            "color": (236, 72, 153),
            "lines": [
                ("Why Prune?", "Removes redundant weights to prevent overfitting, speed up inference & shrink model size."),
                ("", ""),
                ("1. Magnitude Pruning:", "Delete weights if |w| is close to 0 (crude)."),
                ("", ""),
                ("2. Optimal Brain Damage (OBD):", "Uses diagonal Hessian elements (h_kk). Saliency s_k = 0.5 * h_kk * w_k^2. Deletes weights with lowest saliency!"),
                ("", ""),
                ("3. Optimal Brain Surgeon (OBS):", "Uses full inverse Hessian H^-1 to adjust remaining weights.")
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

    # Bottom Summary
    draw.rounded_rectangle([60, 740, width - 60, 960], radius=14, fill=(30, 41, 59), outline=(245, 158, 11), width=2)
    draw.text((90, 755), "★ EXAM CHEAT-SHEET: OBD (OPTIMAL BRAIN DAMAGE) SALIENCY FORMULA", fill=(254, 240, 138), font=card_title_font)
    draw.text((90, 800), "Saliency Formula:  s_k = (1/2) * h_kk * (w_k)^2", fill=(250, 204, 21), font=data_font)
    draw.text((90, 840), "Where: w_k = weight value, h_kk = diagonal 2nd-derivative element from Hessian matrix.", fill=(255, 255, 255), font=data_font)
    draw.text((90, 880), "Procedure: 1. Train network to convergence -> 2. Compute saliency for all weights -> 3. Prune lowest saliency weights.", fill=(56, 189, 248), font=data_font)
    draw.text((90, 920), "Result: Dramatically reduces overfitting, improves generalization, and slashes memory footprint!", fill=(74, 222, 128), font=data_font)

    img.save(output_path, quality=95)
    print(f"Saved Visual: {output_path}")

def render_pruning_notes(output_path):
    from render_notes import create_handwritten_notebook
    create_handwritten_notebook(
        output_path=output_path,
        title="GENERALIZATION & PRUNING (10 MARKS)",
        sections=[
            {
                "heading": "1. What is Generalization in Neural Networks?",
                "highlight": True,
                "content": [
                    "• Definition: The mathematical capability of a trained neural network to correctly",
                    "  interpolate or classify unseen test patterns from the environment.",
                    "• Underfitting: Network capacity is too small (fails on both train & test).",
                    "• Overfitting: Network memorizes training noise (train error ~0, test error huge)."
                ]
            },
            {
                "heading": "2. Cross-Validation (Model Selection)",
                "highlight": False,
                "content": [
                    "• K-Fold Cross Validation: Dataset split into K subsets (typically K=5 or 10).",
                    "• K iterations: Train on K-1 folds, validate on 1 fold. Average the validation error.",
                    "• Early Stopping: Stop backprop training when validation set error starts to rise!"
                ]
            },
            {
                "heading": "3. Network Pruning: Optimal Brain Damage (OBD)",
                "highlight": True,
                "content": [
                    "• Developed by Yann LeCun et al. to delete redundant weights.",
                    "• Assumes diagonal Hessian approximation (neglects off-diagonal elements).",
                    "• Saliency s_k = 0.5 * h_kk * (w_k)^2  (measures increase in error if w_k is deleted).",
                    "• Algorithm: Train net -> compute s_k -> remove smallest s_k -> retrain."
                ]
            },
            {
                "heading": "4. Optimal Brain Surgeon (OBS)",
                "highlight": False,
                "content": [
                    "• Hassibi & Stork extension: Uses FULL inverse Hessian H^-1 (no diagonal shortcut).",
                    "• Not only deletes redundant weight w_q, but simultaneously adjusts all other weights!"
                ]
            }
        ],
        exam_tip="Always write the OBD saliency formula s_k = 0.5 * h_kk * w_k^2 and contrast\nUnderfitting vs Overfitting with a sketch to guarantee full 10 marks!"
    )

if __name__ == "__main__":
    visual_path = "f:/kachara/project final year/exam_study/neural_networks/nn_m4_pruning_visual.jpg"
    notes_path = "f:/kachara/project final year/exam_study/neural_networks/nn_m4_pruning_notes.jpg"
    render_pruning_visual(visual_path)
    render_pruning_notes(notes_path)
