import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, KeepTogether, HRFlowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

def build_pdf():
    pdf_filename = "VIVA_STORY_AND_DICTIONARY_GUIDE.pdf"
    
    # 0.5 inch margins = 36 pt
    doc = SimpleDocTemplate(
        pdf_filename,
        pagesize=letter,
        leftMargin=36,
        rightMargin=36,
        topMargin=36,
        bottomMargin=36
    )

    styles = getSampleStyleSheet()

    # Custom styles
    title_style = ParagraphStyle(
        'MainTitle',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=18,
        leading=22,
        textColor=colors.HexColor('#0f172a'),
        alignment=1, # Centered
        spaceAfter=4
    )

    subtitle_style = ParagraphStyle(
        'SubTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=10,
        leading=13,
        textColor=colors.HexColor('#2563eb'),
        alignment=1,
        spaceAfter=12
    )

    h1_style = ParagraphStyle(
        'H1',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=16,
        textColor=colors.HexColor('#1e3a8a'),
        spaceBefore=10,
        spaceAfter=6
    )

    h2_style = ParagraphStyle(
        'H2',
        parent=styles['Heading3'],
        fontName='Helvetica-Bold',
        fontSize=10.5,
        leading=14,
        textColor=colors.HexColor('#0f172a'),
        spaceBefore=6,
        spaceAfter=3
    )

    body_style = ParagraphStyle(
        'Body',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=12.5,
        textColor=colors.HexColor('#1e293b'),
        spaceAfter=4
    )

    body_bold = ParagraphStyle(
        'BodyBold',
        parent=body_style,
        fontName='Helvetica-Bold'
    )

    callout_style = ParagraphStyle(
        'Callout',
        parent=body_style,
        fontName='Helvetica',
        fontSize=8.5,
        leading=12.5,
        textColor=colors.HexColor('#0f172a')
    )

    table_th = ParagraphStyle(
        'TableTH',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=11,
        textColor=colors.white
    )

    table_term = ParagraphStyle(
        'TableTerm',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8,
        leading=11,
        textColor=colors.HexColor('#1e40af')
    )

    table_sounds = ParagraphStyle(
        'TableSounds',
        parent=styles['Normal'],
        fontName='Helvetica-Oblique',
        fontSize=8,
        leading=11,
        textColor=colors.HexColor('#64748b')
    )

    table_means = ParagraphStyle(
        'TableMeans',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8,
        leading=11,
        textColor=colors.HexColor('#0f172a')
    )

    story = []

    # Header Banner
    story.append(Paragraph("NEURO-SYMBOLIC LEGAL INVARIANT CHECKER", title_style))
    story.append(Paragraph("Formal Verification of Financial Credit Agreements • Complete Plain-English Guide", subtitle_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor('#3b82f6'), spaceBefore=2, spaceAfter=8))

    # SECTION 1: THE SIMPLE STORY
    story.append(Paragraph("📖 1. The Simple Story: What Problem Are We Solving?", h1_style))
    
    # Real-world situation box
    real_world_text = (
        "<b>The Real-World Situation:</b><br/>"
        "Imagine a massive company wants to borrow <b>₹500 Crores</b> from a major bank. "
        "Their corporate legal teams draft a <b>120-page legal contract</b> filled with hundreds of financial rules and covenants.<br/>"
        "Because different legal teams draft different clauses late at night, <b>hidden contradictions slip into the contract</b>:<br/>"
        "• <b>On Page 20 (Section 6.01):</b> The contract states: <i>'If the company acquires a competitor, they are permitted to increase their debt ceiling up to 4.0x their earnings.'</i><br/>"
        "• <b>On Page 85 (Section 6.02):</b> Another clause states: <i>'In no event shall total debt exceed ₹30 Crores whenever earnings drop below ₹8 Crores.'</i>"
    )
    
    rw_table = Table([[Paragraph(real_world_text, callout_style)]], colWidths=[540])
    rw_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#f1f5f9')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#cbd5e1')),
        ('PADDING', (0,0), (-1,-1), 8),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ]))
    story.append(rw_table)
    story.append(Spacer(1, 6))

    # The Disaster Box
    disaster_text = (
        "<b>The Disaster: What Happens When Both Clauses Collide?</b><br/>"
        "Suppose the company earns <b>₹7.75 Crores</b> and borrows <b>₹31 Crores</b> to acquire a supplier.<br/>"
        "• According to <b>Page 20</b>: It is <b>ALLOWED</b> (Leverage Ratio = 31 / 7.75 = 4.0x threshold).<br/>"
        "• According to <b>Page 85</b>: It is <b>ILLEGAL</b> (Debt ₹31 Cr > ₹30 Cr while earnings ₹7.75 Cr < ₹8 Cr).<br/>"
        "<b>Result:</b> The contract is mathematically contradictory! In practice, this ambiguity triggers lawsuits, loan recall defaults, and multi-crore legal disputes."
    )
    disaster_table = Table([[Paragraph(disaster_text, callout_style)]], colWidths=[540])
    disaster_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#fef2f2')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#fecaca')),
        ('PADDING', (0,0), (-1,-1), 8),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ]))
    story.append(disaster_table)
    story.append(Spacer(1, 6))

    # Why LLMs fail
    story.append(Paragraph("<b>Why Can't We Just Use ChatGPT or Claude?</b>", h2_style))
    story.append(Paragraph(
        "1. <b>ChatGPT Guesswork & Hallucinations:</b> Large Language Models predict text probabilistically. While excellent at summarizing essays, they <i>cannot perform rigorous formal mathematical proofs</i>.<br/>"
        "2. <b>Missed Boundary Edge Cases:</b> Standard LLMs will read Section 6.01 and 6.02 and declare: <i>'This agreement looks standard and sound.'</i> They cannot evaluate millions of numerical permutations simultaneously.",
        body_style
    ))
    story.append(Spacer(1, 6))

    # SECTION 2: 3-STEP PIPELINE
    story.append(Paragraph("🧠 2. What YOUR Application Does: The 3-Step Pipeline", h1_style))
    story.append(Paragraph(
        "Our system is a <b>Neuro-Symbolic Legal Invariant Checker</b>. It bridges the intuitive linguistic understanding of modern AI with the mathematical certainty of Microsoft Z3 SMT logic solvers:",
        body_style
    ))

    # Pipeline Diagram Table
    pipe_data = [
        [
            Paragraph("<b>Phase 1: Neural Semantic Parsing</b><br/><font color='#2563eb'>Gemini 2.5 Flash API</font><br/>Acts as a legal translator. Reads raw unstructured text from PDFs and parses covenants into a strict Abstract Syntax Tree (AST) schema.", callout_style),
            Paragraph("<b>Phase 2: Symbolic Verification</b><br/><font color='#16a34a'>Z3 SMT Solver (Microsoft)</font><br/>Translates AST into first-order logic on CPU. Formulates mathematical invariant refutation. Checks all edge cases in under 50 milliseconds.", callout_style),
            Paragraph("<b>Phase 3: Legal Redlining</b><br/><font color='#7c3aed'>Automated Reconciliation</font><br/>Extracts counterexample numerical values ($31M Debt, $7.75M EBITDA) and generates legal redline recommendations.", callout_style)
        ]
    ]
    pipe_table = Table(pipe_data, colWidths=[180, 180, 180])
    pipe_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (0,0), colors.HexColor('#eff6ff')),
        ('BACKGROUND', (1,0), (1,0), colors.HexColor('#f0fdf4')),
        ('BACKGROUND', (2,0), (2,0), colors.HexColor('#faf5ff')),
        ('BOX', (0,0), (0,0), 1, colors.HexColor('#bfdbfe')),
        ('BOX', (1,0), (1,0), 1, colors.HexColor('#bbf7d0')),
        ('BOX', (2,0), (2,0), 1, colors.HexColor('#e9d5ff')),
        ('PADDING', (0,0), (-1,-1), 7),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ]))
    story.append(pipe_table)
    story.append(Spacer(1, 10))

    # SECTION 3: DICTIONARY OF DIFFICULT TERMS
    story.append(Paragraph("📚 3. Dictionary of Difficult Terms (Plain English for Viva)", h1_style))
    story.append(Paragraph("Memorize these simple real-world analogies to answer any professor questions with ease:", body_style))

    dict_data = [
        [Paragraph("Complex Term", table_th), Paragraph("What It Sounds Like", table_th), Paragraph("What It ACTUALLY Means (Simple Analogy)", table_th)],
        [
            Paragraph("<b>Neuro-Symbolic</b>", table_term),
            Paragraph("Sci-Fi Alien brain", table_sounds),
            Paragraph("<b>The Brain + The Calculator:</b> Combining a neural network (Gemini) to read language with a symbolic engine (Z3) to do pure math logic.", table_means)
        ],
        [
            Paragraph("<b>Invariant</b>", table_term),
            Paragraph("Deep mathematical rule", table_sounds),
            Paragraph("<b>A rule that must NEVER be broken:</b> Like a <i>'Never exceed 80 km/h'</i> speed limit. In our app: <i>'Debt ratio must never exceed 3.5x'</i>.", table_means)
        ],
        [
            Paragraph("<b>SMT Solver (Z3)</b>", table_term),
            Paragraph("Abstract research tool", table_sounds),
            Paragraph("<b>A hyper-fast logic calculator built by Microsoft:</b> You give it 50 rules and it verifies whether all rules can hold simultaneously without contradiction.", table_means)
        ],
        [
            Paragraph("<b>AST</b><br/>(Abstract Syntax Tree)", table_term),
            Paragraph("Complex data structure", table_sounds),
            Paragraph("<b>The mathematical skeleton:</b> Converts paragraphs of legal text into clean variables like <code>LeverageRatio = Debt / EBITDA</code>.", table_means)
        ],
        [
            Paragraph("<b>Counterexample</b>", table_term),
            Paragraph("Theoretical proof item", table_sounds),
            Paragraph("<b>The proof of guilt:</b> When Z3 finds a flaw, it prints the exact numbers: <i>'At Debt = $31M and EBITDA = $7.75M, the contract breaks!'</i>", table_means)
        ],
        [
            Paragraph("<b>Refutation Principle</b>", table_term),
            Paragraph("Formal logic method", table_sounds),
            Paragraph("<b>Proving safety by searching for a bug:</b> We ask Z3: <i>'Can you find ANY scenario where rules break?'</i> If Z3 says NO (UNSAT), the contract is proven safe.", table_means)
        ],
        [
            Paragraph("<b>Covenant</b>", table_term),
            Paragraph("Medieval legal oath", table_sounds),
            Paragraph("<b>A binding promise in a loan:</b> e.g., <i>'The borrower promises to keep at least ₹10 Crores in their bank account at all times.'</i>", table_means)
        ],
        [
            Paragraph("<b>EBITDA</b>", table_term),
            Paragraph("Wall Street buzzword", table_sounds),
            Paragraph("<b>Operational Cash Profit:</b> Earnings Before Interest, Taxes, Depreciation & Amortization. Basically: how much cash the core business generates.", table_means)
        ],
        [
            Paragraph("<b>Leverage Ratio</b>", table_term),
            Paragraph("Financial metric", table_sounds),
            Paragraph("<b>Debt divided by Profit (Debt / EBITDA):</b> If a company owes ₹30 Cr and earns ₹10 Cr, their leverage ratio is 3.0x.", table_means)
        ],
        [
            Paragraph("<b>Redlining</b>", table_term),
            Paragraph("Document editing", table_sounds),
            Paragraph("<b>Automated clause fix:</b> Marking flawed legal text and inserting clean conflict-override phrases (e.g. <i>'Subject to Section 6.02'</i>).", table_means)
        ]
    ]

    dict_table = Table(dict_data, colWidths=[105, 100, 335])
    dict_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#1e40af')),
        ('PADDING', (0,0), (-1,-1), 4),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#cbd5e1')),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#f8fafc')]),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ]))
    story.append(dict_table)
    story.append(Spacer(1, 10))

    # SECTION 4: THE 1-MINUTE PITCH
    story.append(Paragraph("🎯 4. The 1-Minute Pitch (Memorize This for Your Viva!)", h1_style))
    
    pitch_text = (
        "<i>\"Sir, large financial credit agreements span hundreds of pages and contain complex financial formulas. "
        "Human lawyers frequently make drafting mistakes where two separate clauses contradict each other.<br/><br/>"
        "Large Language Models like ChatGPT cannot reliably detect these issues because they hallucinate and cannot perform formal mathematical proofs.<br/><br/>"
        "Our project implements a <b>Neuro-Symbolic architecture</b>:<br/>"
        "1. <b>Gemini AI</b> extracts unstructured contract covenants into a formal mathematical syntax tree.<br/>"
        "2. Microsoft's <b>Z3 SMT solver</b> executes mathematical refutation logic on CPU in milliseconds to prove whether invariants can ever be broken.<br/>"
        "3. When a conflict exists, our system pinpoints the exact numerical counterexample and generates automated legal redlines to fix the contract before signing.\"</i>"
    )
    pitch_table = Table([[Paragraph(pitch_text, callout_style)]], colWidths=[540])
    pitch_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#eff6ff')),
        ('BOX', (0,0), (-1,-1), 1.5, colors.HexColor('#2563eb')),
        ('PADDING', (0,0), (-1,-1), 9),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ]))
    story.append(pitch_table)

    # Build document
    doc.build(story)
    print(f"Generated successfully: {pdf_filename}")

if __name__ == "__main__":
    build_pdf()
