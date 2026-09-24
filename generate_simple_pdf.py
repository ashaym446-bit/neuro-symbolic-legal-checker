import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch

def build_simple_pdf():
    pdf_filename = "SIMPLE_PROJECT_EXPLANATION_GUIDE.pdf"
    doc = SimpleDocTemplate(
        pdf_filename,
        pagesize=letter,
        rightMargin=45, leftMargin=45,
        topMargin=45, bottomMargin=45
    )

    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        'MainTitle',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=22,
        leading=26,
        textColor=colors.HexColor('#1e40af'),
        alignment=1,
        spaceAfter=6
    )

    subtitle_style = ParagraphStyle(
        'SubTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Oblique',
        fontSize=11,
        leading=15,
        textColor=colors.HexColor('#64748b'),
        alignment=1,
        spaceAfter=20
    )

    h1_style = ParagraphStyle(
        'H1',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=14,
        leading=18,
        textColor=colors.HexColor('#0f172a'),
        spaceBefore=14,
        spaceAfter=8
    )

    h2_style = ParagraphStyle(
        'H2',
        parent=styles['Heading3'],
        fontName='Helvetica-Bold',
        fontSize=11.5,
        leading=15,
        textColor=colors.HexColor('#2563eb'),
        spaceBefore=10,
        spaceAfter=4
    )

    body_style = ParagraphStyle(
        'Body',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9.5,
        leading=13.5,
        textColor=colors.HexColor('#1e293b'),
        spaceAfter=6
    )

    bullet_style = ParagraphStyle(
        'Bullet',
        parent=body_style,
        leftIndent=15,
        spaceAfter=4
    )

    highlight_box_style = ParagraphStyle(
        'Highlight',
        parent=body_style,
        fontName='Helvetica-Bold',
        fontSize=11,
        leading=15,
        textColor=colors.HexColor('#1e3a8a')
    )

    table_header_style = ParagraphStyle(
        'TH',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9,
        leading=12,
        textColor=colors.white
    )

    table_cell_style = ParagraphStyle(
        'TC',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=11.5,
        textColor=colors.HexColor('#0f172a')
    )

    table_bold_style = ParagraphStyle(
        'TCB',
        parent=table_cell_style,
        fontName='Helvetica-Bold',
        textColor=colors.HexColor('#1d4ed8')
    )

    story = []

    # Title
    story.append(Paragraph("Neuro-Symbolic Legal Invariant Checker", title_style))
    story.append(Paragraph("Plain-English Project Story, Dictionary of Terms & Professor Viva Cheat Sheet", subtitle_style))

    # Section 1
    story.append(Paragraph("1. The Entire Project in ONE Simple Sentence", h1_style))
    
    quote_data = [[
        Paragraph(
            "<b>\"This project is an automated bug-checker for multi-million dollar bank loan contracts — "
            "it finds mathematical contradictions that human lawyers accidentally wrote.\"</b><br/><br/>"
            "<i>Think of it like Grammarly, but instead of checking spelling mistakes, it checks whether "
            "the contract's financial math rules clash with each other.</i>",
            highlight_box_style
        )
    ]]
    t_quote = Table(quote_data, colWidths=[7.2 * inch])
    t_quote.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#eff6ff')),
        ('BOX', (0,0), (-1,-1), 1.5, colors.HexColor('#3b82f6')),
        ('PADDING', (0,0), (-1,-1), 10),
    ]))
    story.append(t_quote)
    story.append(Spacer(1, 10))

    # Section 2: Financial Terms Dictionary
    story.append(Paragraph("2. The 'Cheat Sheet' Dictionary: Financial Terms", h1_style))
    story.append(Paragraph("Every financial word explained in plain everyday concepts:", body_style))

    fin_terms = [
        ["Word", "What It Actually Means", "Real-Life Example"],
        [
            Paragraph("Contract / Agreement", table_bold_style),
            Paragraph("A legal deal signed between a Bank and a Company.", table_cell_style),
            Paragraph("The bank says: 'Here is $50M, but follow our rules.'", table_cell_style)
        ],
        [
            Paragraph("Borrower vs. Lender", table_bold_style),
            Paragraph("Borrower = Company taking money.<br/>Lender = Bank giving money.", table_cell_style),
            Paragraph("If you take a home loan from SBI, you are Borrower, SBI is Lender.", table_cell_style)
        ],
        [
            Paragraph("Covenant", table_bold_style),
            Paragraph("A strict promise / rule in the contract.", table_cell_style),
            Paragraph("'Rule 1: Keep your total debt under a safe ceiling.'", table_cell_style)
        ],
        [
            Paragraph("EBITDA", table_bold_style),
            Paragraph("<b>Pure Profit</b> from running the business.<br/>(Earnings Before Interest, Taxes, Depreciation)", table_cell_style),
            Paragraph("If you sell $100 of burgers and spent $60 on ingredients, your EBITDA is $40.", table_cell_style)
        ],
        [
            Paragraph("Total Debt", table_bold_style),
            Paragraph("Total borrowed loan money owed to banks.", table_cell_style),
            Paragraph("Loans from Bank A ($10M) + Bank B ($20M) = $30M Total Debt.", table_cell_style)
        ],
        [
            Paragraph("Leverage Ratio", table_bold_style),
            Paragraph("How many times bigger your debt is compared to profit (Debt / EBITDA).", table_cell_style),
            Paragraph("Debt of $30M divided by Profit of $10M = 3.0x Leverage Ratio.", table_cell_style)
        ],
        [
            Paragraph("Interest Expense", table_bold_style),
            Paragraph("The monthly fee/interest you pay the bank for borrowing.", table_cell_style),
            Paragraph("Paying 5% interest fee on your loan.", table_cell_style)
        ],
        [
            Paragraph("Grace Period", table_bold_style),
            Paragraph("Extra days given to pay if you miss a due date.", table_cell_style),
            Paragraph("'15-day cure window before the bank can take legal action.'", table_cell_style)
        ],
        [
            Paragraph("Acceleration", table_bold_style),
            Paragraph("The bank demanding ALL the loan money back TODAY.", table_cell_style),
            Paragraph("Instead of monthly installments, the bank says: 'Pay all $50M right now!'", table_cell_style)
        ],
        [
            Paragraph("Redline", table_bold_style),
            Paragraph("The corrected replacement clause written to fix the bug.", table_cell_style),
            Paragraph("Striking through bad contract text and inserting the fix.", table_cell_style)
        ]
    ]

    t_fin = Table(fin_terms, colWidths=[1.8*inch, 2.7*inch, 2.7*inch])
    t_fin.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#1e40af')),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#cbd5e1')),
        ('PADDING', (0,0), (-1,-1), 5),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#f8fafc')])
    ]))
    story.append(t_fin)
    story.append(Spacer(1, 10))

    # Section 3: Technical Terms Dictionary
    story.append(Paragraph("3. The 'Cheat Sheet' Dictionary: Technical & AI Terms", h1_style))
    tech_terms = [
        ["Word", "What It Actually Means", "Real-Life Example"],
        [
            Paragraph("Invariant", table_bold_style),
            Paragraph("A golden safety rule that must NEVER, EVER be broken.", table_cell_style),
            Paragraph("In a car: 'Speed must never exceed 200 km/h.'<br/>In a loan: 'Debt must never exceed the cap.'", table_cell_style)
        ],
        [
            Paragraph("SMT Solver (Z3)", table_bold_style),
            Paragraph("A supercomputer math prover built by Microsoft Research.", table_cell_style),
            Paragraph("Checks all possible numbers from -inf to +inf to prove if a formula can break.", table_cell_style)
        ],
        [
            Paragraph("SAT (Satisfiable)", table_bold_style),
            Paragraph("<b>'I found a bug!'</b><br/>The solver found numbers that break the contract.", table_cell_style),
            Paragraph("'When Profit = $7.8M, Rule A allows $31.2M, but Rule B caps at $30M. SAT!'", table_cell_style)
        ],
        [
            Paragraph("UNSAT (Unsatisfiable)", table_bold_style),
            Paragraph("<b>'100% Safe!'</b><br/>It is mathematically impossible to break the rule.", table_cell_style),
            Paragraph("The solver proves zero loopholes exist under any scenario.", table_cell_style)
        ],
        [
            Paragraph("Counterexample", table_bold_style),
            Paragraph("The exact mathematical numbers that trigger the loophole.", table_cell_style),
            Paragraph("Proof values: [Total Debt = $31.2M, EBITDA = $7.8M].", table_cell_style)
        ],
        [
            Paragraph("Neuro-Symbolic", table_bold_style),
            Paragraph("Combining a <b>Reader</b> (Neural) with a <b>Calculator</b> (Symbolic).", table_cell_style),
            Paragraph("Gemini reads English prose -> Z3 solves pure math equations.", table_cell_style)
        ],
        [
            Paragraph("AST / DSL", table_bold_style),
            Paragraph("Turning messy English prose into clean mathematical formulas.", table_cell_style),
            Paragraph("Translating 'Debt cannot exceed twice profit' into debt <= 2 * profit.", table_cell_style)
        ]
    ]

    t_tech = Table(tech_terms, colWidths=[1.8*inch, 2.7*inch, 2.7*inch])
    t_tech.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#0f172a')),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#cbd5e1')),
        ('PADDING', (0,0), (-1,-1), 5),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#f8fafc')])
    ]))
    story.append(t_tech)
    story.append(Spacer(1, 10))

    # Section 4: The Real-Life Story
    story.append(Paragraph("4. The Real-Life Story: Where Does the Bug Come From?", h1_style))
    story.append(Paragraph(
        "A 100-page loan contract is written by multiple lawyers across different teams. Contradictions happen naturally:",
        body_style
    ))
    story.append(Paragraph("• <b>Lawyer 1 (Section 6.01, Page 10):</b> <i>'During an acquisition, you can borrow up to 4.0 times your profit.'</i>", bullet_style))
    story.append(Paragraph("• <b>Lawyer 2 (Section 6.02, Page 60):</b> <i>'Under no circumstances can total debt exceed $30,000,000 if profit is under $8,000,000.'</i>", bullet_style))
    story.append(Paragraph(
        "<b>What happens in real life if the company makes $7.8 Million in profit?</b><br/>"
        "1. Lawyer 1's rule says the company can legally borrow: 4.0 * $7.8M = <b>$31.2 Million</b>.<br/>"
        "2. Lawyer 2's rule says debt is strictly capped at: <b>$30.0 Million</b>.<br/>"
        "The company borrows $31M thinking they followed the rules, but the bank claims they breached the contract! "
        "This leads to lawsuits worth millions of dollars. Our software catches this in 19 milliseconds.",
        body_style
    ))
    story.append(Spacer(1, 8))

    # Section 5: Why Not Normal ChatGPT?
    story.append(Paragraph("5. Why Can't We Just Use Normal ChatGPT / LLMs?", h1_style))
    story.append(Paragraph(
        "If you paste a 100-page contract into ChatGPT and ask: <i>'Are there any math bugs?'</i>, <b>ChatGPT will guess</b>. "
        "LLMs are text predictors, not math calculators. They hallucinate and miss subtle edge cases (like division by zero "
        "when interest expense is $0). In banking, an 85% accurate tool is a 100% failure. You need 100% mathematical certainty.",
        body_style
    ))

    # Section 6: How the App Works
    story.append(Paragraph("6. How Your Project Works (The 3 Easy Steps)", h1_style))
    story.append(Paragraph("• <b>STEP 1: GEMINI (The Reader / Neural):</b> Reads messy English legal text and compiles it into clean math formulas (e.g. debt <= 4.0 * ebitda).", bullet_style))
    story.append(Paragraph("• <b>STEP 2: Z3 SMT SOLVER (The Calculator / Symbolic):</b> Solves the formulas across all numbers in 19 milliseconds. It mathematically proves whether any number can trigger a contradiction.", bullet_style))
    story.append(Paragraph("• <b>STEP 3: THE EXPLAINER (The Lawyer):</b> Takes Z3's counterexample numbers and drafts a plain-English redline amendment to cure the contract.", bullet_style))
    story.append(Spacer(1, 8))

    # Section 7: Viva / Professor Q&A
    story.append(Paragraph("7. Professor Defense / Viva Voce Cheat Sheet", h1_style))
    
    viva_qa = [
        ("Q1: What is your project about?",
         "\"Sir, financial loan contracts are hundreds of pages long and frequently contain contradictory borrowing limits. My project uses Gemini AI to read the contract into math formulas, and the Z3 SMT solver to mathematically prove whether any loopholes exist with 100% certainty.\""),
        ("Q2: What is an Invariant?",
         "\"An invariant is a safety rule that must never be broken under any circumstances — for example, ensuring that a borrower's total debt never exceeds the bank's maximum safety ceiling.\""),
        ("Q3: What is EBITDA?",
         "\"EBITDA stands for Earnings Before Interest, Taxes, Depreciation, and Amortization. In simple words, it is the company's operating cash profit from running its core business.\""),
        ("Q4: Why did you use Z3 instead of just asking Gemini?",
         "\"Because Gemini is an LLM — it hallucinates and cannot perform mathematical proofs. Z3 is an industrial SMT theorem prover from Microsoft that provides 100% mathematical certainty with zero hallucinations.\""),
        ("Q5: What did YOU do as a researcher?",
         "\"I designed the formal domain schema that translates legal English into SMT mathematics, formulated the invariant proof equations, built the Z3 verification engine, and benchmarked that our Neuro-Symbolic approach achieves 100% mathematical soundness compared to 62% for pure LLMs.\"")
    ]

    for q, a in viva_qa:
        story.append(Paragraph(f"<b>{q}</b>", h2_style))
        story.append(Paragraph(a, body_style))

    doc.build(story)
    print(f"Generated: {pdf_filename} ({os.path.getsize(pdf_filename)} bytes)")

if __name__ == '__main__':
    build_simple_pdf()
