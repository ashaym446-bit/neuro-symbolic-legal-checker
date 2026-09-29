import os
from PIL import Image, ImageDraw, ImageFont
from render_notes import create_handwritten_notebook

FONT_TITLE = "C:/Windows/Fonts/segoeuib.ttf"
FONT_BODY = "C:/Windows/Fonts/segoeui.ttf"
FONT_CODE = "C:/Windows/Fonts/consola.ttf"

def make_visual_card(draw, cx, cy, card_w, card_h, color, title, subtitle, lines, fonts):
    draw.rounded_rectangle([cx, cy, cx + card_w, cy + card_h], radius=14, fill=(30, 41, 59), outline=color, width=2)
    draw.rounded_rectangle([cx, cy, cx + card_w, cy + 65], radius=14, fill=color)
    draw.rectangle([cx, cy + 45, cx + card_w, cy + 65], fill=color)

    draw.text((cx + 15, cy + 12), title, fill=(255, 255, 255), font=fonts["card_title"])
    draw.text((cx + 15, cy + 40), subtitle, fill=(254, 240, 138), font=fonts["data"])

    dy = cy + 85
    for item in lines:
        if isinstance(item, (list, tuple)):
            if len(item) == 0:
                lbl, val = "", ""
            elif len(item) == 1:
                lbl, val = "", str(item[0])
            else:
                lbl, val = str(item[0]), str(item[1])
        else:
            lbl, val = "", str(item)
        
        if lbl:
            draw.text((cx + 20, dy), lbl, fill=(56, 189, 248), font=fonts["card_title"])
            dy += 28
        if val:
            words = val.split(" ")
            cur = ""
            for w in words:
                if len(cur + " " + w) > 34:
                    draw.text((cx + 20, dy), cur, fill=(226, 232, 240), font=fonts["body"])
                    dy += 24
                    cur = w
                else:
                    cur = (cur + " " + w).strip()
            if cur:
                draw.text((cx + 20, dy), cur, fill=(226, 232, 240), font=fonts["body"])
                dy += 26
        dy += 6

# ==============================================================================
# 1. CD Module 5 - Topic 1: Run-Time Environments & Storage Allocation
# ==============================================================================
def render_cd_m5_runtime():
    v_path = "f:/kachara/project final year/exam_study/compiler_design/cd_m5_runtime_visual.jpg"
    n_path = "f:/kachara/project final year/exam_study/compiler_design/cd_m5_runtime_notes.jpg"

    img = Image.new("RGB", (1600, 1000), (15, 23, 42))
    draw = ImageDraw.Draw(img)
    fonts = {
        "title": ImageFont.truetype(FONT_TITLE, 36),
        "sub": ImageFont.truetype(FONT_BODY, 22),
        "card_title": ImageFont.truetype(FONT_TITLE, 24),
        "data": ImageFont.truetype(FONT_CODE, 19),
        "body": ImageFont.truetype(FONT_BODY, 19)
    }

    draw.text((60, 30), "COMPILER DESIGN: RUN-TIME STORAGE ORGANIZATION & ALLOCATION", fill=(255, 255, 255), font=fonts["title"])
    draw.text((60, 78), "Module 5: How the target machine's logical address space is subdivided and managed during execution.", fill=(56, 189, 248), font=fonts["sub"])

    cards = [
        {
            "title": "1. STORAGE SUBDIVISIONS",
            "subtitle": "Target Memory Map Layout",
            "color": (59, 130, 246),
            "lines": [
                ("1. Code Area (Static):", "Holds generated target machine instructions. Read-only fixed size."),
                ("", ""),
                ("2. Static Data Area:", "Holds global & static constants known at compile time."),
                ("", ""),
                ("3. Stack (Grows Down):", "Holds Activation Records for function calls (LIFO). Automatic variables."),
                ("", ""),
                ("4. Heap (Grows Up):", "Dynamically allocated memory (malloc / new). Lifetimes outlive function calls.")
            ]
        },
        {
            "title": "2. ACTIVATION RECORD (AR)",
            "subtitle": "Frame Structure per Function Call",
            "color": (16, 185, 129),
            "lines": [
                ("What is an AR?", "A contiguous block of memory allocated when a procedure is called."),
                ("", ""),
                ("Fields from Top to Bottom:", "• Actual Parameters (passed by caller)"),
                ("• Returned Value (to caller)", ""),
                ("• Control Link (Old Frame Pointer FP)", ""),
                ("• Access Link (Static nesting scope)", ""),
                ("• Saved Machine Status (Registers, PC)", ""),
                ("• Local Variables", ""),
                ("• Temporaries (expression evaluation)", "")
            ]
        },
        {
            "title": "3. ALLOCATION STRATEGIES",
            "subtitle": "Static vs Stack vs Heap",
            "color": (245, 158, 11),
            "lines": [
                ("1. Static Allocation:", "Fixed addresses bound at compile time (Fortran). No recursion allowed!"),
                ("", ""),
                ("2. Stack Allocation:", "Frames pushed on call, popped on return (C, Pascal, Java). Supports recursion!"),
                ("", ""),
                ("3. Heap Allocation:", "Deallocated in any arbitrary order. Requires Garbage Collector or manual free.")
            ]
        }
    ]

    for i, c in enumerate(cards):
        make_visual_card(draw, 60 + i * 500, 130, 460, 580, c["color"], c["title"], c["subtitle"], c["lines"], fonts)

    draw.rounded_rectangle([60, 740, 1540, 960], radius=14, fill=(30, 41, 59), outline=(99, 102, 241), width=2)
    draw.text((90, 755), "★ EXAM SUMMARY: CALLING SEQUENCE & FRAME POINTER (FP) (5-10 MARKS)", fill=(165, 180, 252), font=fonts["card_title"])
    draw.text((90, 800), "• Calling Sequence: Code executed by caller & callee to set up the new activation record on procedure invocation.", fill=(255, 255, 255), font=fonts["data"])
    draw.text((90, 840), "• Return Sequence: Restores saved machine registers, updates return value, and pops the activation record off stack.", fill=(56, 189, 248), font=fonts["data"])
    draw.text((90, 880), "• Control Link (Dynamic Link): Points to the activation record of the CALLER (used for stack unwinding).", fill=(250, 204, 21), font=fonts["data"])
    draw.text((90, 920), "• Access Link (Static Link): Points to the activation record of the static nesting scope (used to access non-local variables).", fill=(74, 222, 128), font=fonts["data"])

    img.save(v_path, quality=95)
    print(f"Saved: {v_path}")

    create_handwritten_notebook(
        output_path=n_path,
        title="RUN-TIME STORAGE ALLOCATION (10 MARKS)",
        sections=[
            {
                "heading": "1. Storage Organization",
                "highlight": True,
                "content": [
                    "• The compiler gets a logical address space from OS divided into 4 regions:",
                    "  1. Code (Fixed size, executable instructions).",
                    "  2. Static data (Global variables).",
                    "  3. Heap (Dynamically allocated data via malloc/new, grows downwards).",
                    "  4. Stack (Activation records, grows upwards towards heap)."
                ]
            },
            {
                "heading": "2. Activation Record Structure (Must Draw in Exam!)",
                "highlight": True,
                "content": [
                    "• Actual parameters (passed by caller).",
                    "• Returned values.",
                    "• Control link (Dynamic link: points to caller's frame).",
                    "• Access link (Static link: for lexical scope resolution).",
                    "• Saved machine status (program counter PC + CPU registers).",
                    "• Local data & Temporaries."
                ]
            },
            {
                "heading": "3. Comparison of Allocation Strategies",
                "highlight": False,
                "content": [
                    "• Static: Compile-time binding. Fast, but NO recursion and fixed array sizes.",
                    "• Stack: Run-time LIFO management. Allows recursion, nested scopes, dynamic local arrays.",
                    "• Heap: Arbitrary lifetime allocation. Overhead of fragmentation & garbage collection."
                ]
            }
        ],
        exam_tip="Draw the complete memory layout (Code | Static | Heap -> <- Stack) and the 7-field\nActivation Record diagram to score full 10 marks!"
    )

# ==============================================================================
# 2. CD Module 5 - Topic 2: Basic Blocks & Flow Graphs
# ==============================================================================
def render_cd_m5_basic_blocks():
    v_path = "f:/kachara/project final year/exam_study/compiler_design/cd_m5_basic_blocks_visual.jpg"
    n_path = "f:/kachara/project final year/exam_study/compiler_design/cd_m5_basic_blocks_notes.jpg"

    img = Image.new("RGB", (1600, 1000), (15, 23, 42))
    draw = ImageDraw.Draw(img)
    fonts = {
        "title": ImageFont.truetype(FONT_TITLE, 36),
        "sub": ImageFont.truetype(FONT_BODY, 22),
        "card_title": ImageFont.truetype(FONT_TITLE, 24),
        "data": ImageFont.truetype(FONT_CODE, 19),
        "body": ImageFont.truetype(FONT_BODY, 19)
    }

    draw.text((60, 30), "COMPILER DESIGN: BASIC BLOCKS & FLOW GRAPHS (NUMERICAL)", fill=(255, 255, 255), font=fonts["title"])
    draw.text((60, 78), "Module 5: How intermediate 3AC instructions are partitioned into basic blocks and represented as a Control Flow Graph (CFG).", fill=(56, 189, 248), font=fonts["sub"])

    cards = [
        {
            "title": "1. WHAT IS A BASIC BLOCK?",
            "subtitle": "Single-Entry, Single-Exit",
            "color": (59, 130, 246),
            "lines": [
                ("Strict Definition:", "A sequence of consecutive three-address statements in which:"),
                ("", ""),
                ("• Rule 1 (Entry):", "Flow of control enters ONLY at the very first instruction."),
                ("", ""),
                ("• Rule 2 (Exit):", "Control leaves the block ONLY at the last instruction (no jumps in the middle!)."),
                ("", ""),
                ("Consequence:", "If statement 1 executes, ALL subsequent statements in the block are guaranteed to execute in order.")
            ]
        },
        {
            "title": "2. ALGORITHM TO FIND LEADERS",
            "subtitle": "The 3 Rules (Must Memorize!)",
            "color": (16, 185, 129),
            "lines": [
                ("The First statement in 3AC is a Leader.", ""),
                ("", ""),
                ("Rule 2 (Targets):", "Any statement that is the TARGET of a conditional or unconditional goto is a Leader."),
                ("", ""),
                ("Rule 3 (Successors):", "Any statement that IMMEDIATELY FOLLOWS a conditional or unconditional goto is a Leader."),
                ("", ""),
                ("Building the Block:", "A basic block starts at a Leader and extends up to (but not including) the next Leader!")
            ]
        },
        {
            "title": "3. CONTROL FLOW GRAPH (CFG)",
            "subtitle": "Directed Edges Between Blocks",
            "color": (245, 158, 11),
            "lines": [
                ("Nodes:", "Each Basic Block B_i is a node in the graph."),
                ("", ""),
                ("Edges B_i -> B_j exist if:", "• There is a conditional/unconditional jump from end of B_i to B_j."),
                ("• OR B_j immediately follows B_i in linear order, and B_i does not end in unconditional goto."),
                ("", ""),
                ("Initial Node:", "Block containing statement 1.")
            ]
        }
    ]

    for i, c in enumerate(cards):
        make_visual_card(draw, 60 + i * 500, 130, 460, 580, c["color"], c["title"], c["subtitle"], c["lines"], fonts)

    draw.rounded_rectangle([60, 740, 1540, 960], radius=14, fill=(30, 41, 59), outline=(236, 72, 153), width=2)
    draw.text((90, 755), "★ EXAM NUMERICAL EXAMPLE: PARTITIONING 3AC STATEMENTS (10 MARKS)", fill=(244, 114, 182), font=fonts["card_title"])
    draw.text((90, 800), "Code: (1) i = 1  (2) j = 1  (3) t1 = 10 * i  (4) t2 = t1 + j  (5) if t2 < 100 goto (3)  (6) i = i + 1  (7) goto (2)", fill=(250, 204, 21), font=fonts["data"])
    draw.text((90, 840), "Leaders: (1) First stmt; (3) Target of goto in stmt 5; (6) Follows goto in stmt 5; (2) Target of goto in stmt 7.", fill=(255, 255, 255), font=fonts["data"])
    draw.text((90, 880), "Basic Blocks: B1 = {(1)}, B2 = {(2)}, B3 = {(3), (4), (5)}, B4 = {(6), (7)}.", fill=(56, 189, 248), font=fonts["data"])
    draw.text((90, 920), "Flow Graph Edges: B1 -> B2;  B2 -> B3;  B3 -> B3 (loop!);  B3 -> B4;  B4 -> B2 (outer loop!).", fill=(74, 222, 128), font=fonts["data"])

    img.save(v_path, quality=95)
    print(f"Saved: {v_path}")

    create_handwritten_notebook(
        output_path=n_path,
        title="BASIC BLOCKS & FLOW GRAPHS (10 MARKS)",
        sections=[
            {
                "heading": "1. Definition of Basic Block",
                "highlight": True,
                "content": [
                    "• A sequence of consecutive three-address statements with single entry & single exit.",
                    "• Execution enters at first instruction and leaves at last instruction.",
                    "• No branch or jump can land inside the block except at the first statement."
                ]
            },
            {
                "heading": "2. Algorithm to Partition 3AC into Basic Blocks",
                "highlight": True,
                "content": [
                    "Step 1: Identify LEADERS using 3 rules:",
                    "  Rule 1: First statement of 3AC is a leader.",
                    "  Rule 2: Target of any conditional or unconditional goto is a leader.",
                    "  Rule 3: Any statement immediately following a goto is a leader.",
                    "Step 2: Construct Blocks:",
                    "  Each basic block starts with a leader and includes all statements up to",
                    "  (but excluding) the next leader or the end of the program."
                ]
            },
            {
                "heading": "3. Constructing Control Flow Graph (CFG)",
                "highlight": False,
                "content": [
                    "• Directed graph where nodes are basic blocks and edges represent flow of control.",
                    "• Directed edge from B1 to B2 exists if control can transfer from B1 to B2:",
                    "  (a) via jump: conditional/unconditional goto.",
                    "  (b) via fall-through: B2 immediately follows B1 in sequential code."
                ]
            }
        ],
        exam_tip="Always list the 3 Leader Rules, identify the leaders explicitly by line number,\nand draw the boxed Flow Graph with directed arrows for full 10 marks!"
    )

# ==============================================================================
# 3. CD Module 5 - Topic 3: Code Generation & Register Allocation (DAGs)
# ==============================================================================
def render_cd_m5_codegen():
    v_path = "f:/kachara/project final year/exam_study/compiler_design/cd_m5_codegen_visual.jpg"
    n_path = "f:/kachara/project final year/exam_study/compiler_design/cd_m5_codegen_notes.jpg"

    img = Image.new("RGB", (1600, 1000), (15, 23, 42))
    draw = ImageDraw.Draw(img)
    fonts = {
        "title": ImageFont.truetype(FONT_TITLE, 36),
        "sub": ImageFont.truetype(FONT_BODY, 22),
        "card_title": ImageFont.truetype(FONT_TITLE, 24),
        "data": ImageFont.truetype(FONT_CODE, 19),
        "body": ImageFont.truetype(FONT_BODY, 19)
    }

    draw.text((60, 30), "COMPILER DESIGN: CODE GENERATION, REGISTER ALLOCATION & DAGs", fill=(255, 255, 255), font=fonts["title"])
    draw.text((60, 78), "Module 5: The final synthesis phase. Generating target assembly instructions from basic blocks.", fill=(56, 189, 248), font=fonts["sub"])

    cards = [
        {
            "title": "1. CODE GENERATOR ISSUES",
            "subtitle": "Major Challenges in Target Code",
            "color": (59, 130, 246),
            "lines": [
                ("1. Input IR Quality:", "Preserving semantic meaning of 3AC while minimizing instructions."),
                ("", ""),
                ("2. Target Machine Architecture:", "CISC vs RISC instruction set, addressing modes, cost of memory accesses."),
                ("", ""),
                ("3. Instruction Selection:", "Choosing uniform, efficient assembly opcodes (e.g. INC x vs ADD x, 1)."),
                ("", ""),
                ("4. Register Allocation:", "Registers are fastest memory but scarce. Deciding which values stay in registers.")
            ]
        },
        {
            "title": "2. REGISTER ALLOCATION",
            "subtitle": "getreg() & Next-Use Info",
            "color": (16, 185, 129),
            "lines": [
                ("Register Descriptor (R_desc):", "Tracks which variables are currently stored in register R."),
                ("", ""),
                ("Address Descriptor (A_desc):", "Tracks all memory locations where variable x can be found (register, stack, memory)."),
                ("", ""),
                ("getreg(x = y op z):", "Determines best register R to hold the result of operation op:"),
                ("• If y is already in R and has no next-use, reuse R!"),
                ("• Otherwise pick an empty register or spill least needed variable.")
            ]
        },
        {
            "title": "3. DAGs IN CODE GENERATION",
            "subtitle": "Basic Block Optimization",
            "color": (245, 158, 11),
            "lines": [
                ("Why build a DAG for basic block?", ""),
                ("• Eliminates Common Subexpressions: Identical calculations share the same node."),
                ("", ""),
                ("• Eliminates Dead Code: Nodes with no attached live variables produce no code!"),
                ("", ""),
                ("• Reordering Instructions: Evaluates sub-trees in an order that minimizes register spilling.")
            ]
        }
    ]

    for i, c in enumerate(cards):
        make_visual_card(draw, 60 + i * 500, 130, 460, 580, c["color"], c["title"], c["subtitle"], c["lines"], fonts)

    draw.rounded_rectangle([60, 740, 1540, 960], radius=14, fill=(30, 41, 59), outline=(16, 185, 129), width=2)
    draw.text((90, 755), "★ 10-MARK EXAM CODE GENERATION TEMPLATE: SIMPLE CODE GENERATOR", fill=(110, 231, 183), font=fonts["card_title"])
    draw.text((90, 800), "Statement: x = y + z  -> Assembly generated using getreg():", fill=(250, 204, 21), font=fonts["data"])
    draw.text((90, 840), "1. Call L = getreg(x = y + z). If y is not in L, generate:  MOV y, L", fill=(255, 255, 255), font=fonts["data"])
    draw.text((90, 880), "2. Generate:  ADD z, L  (where z is location from address descriptor of z)", fill=(56, 189, 248), font=fonts["data"])
    draw.text((90, 920), "3. Update address descriptor: x is now in L. If y or z have no next-use, clear their descriptors from registers!", fill=(74, 222, 128), font=fonts["data"])

    img.save(v_path, quality=95)
    print(f"Saved: {v_path}")

    create_handwritten_notebook(
        output_path=n_path,
        title="CODE GENERATION & REGISTERS (10 MARKS)",
        sections=[
            {
                "heading": "1. Issues in Code Generator Design",
                "highlight": True,
                "content": [
                    "• Target Machine: Memory-to-memory vs register-to-register architecture.",
                    "• Instruction Selection: High quality code requires selecting optimal instructions.",
                    "• Register Allocation vs Assignment:",
                    "  - Allocation: Selecting the set of variables that will reside in registers.",
                    "  - Assignment: Picking the specific hardware register (R0, R1) for each variable.",
                    "• Evaluation Order: Sequence of statement execution affects register pressure."
                ]
            },
            {
                "heading": "2. Register & Address Descriptors",
                "highlight": True,
                "content": [
                    "• Register Descriptor: Tracks which variables are currently stored in register R.",
                    "• Address Descriptor: Tracks current location(s) of variable x (e.g., register R0, memory M_x).",
                    "• getreg() Function: Selects register L for instruction x = y op z."
                ]
            },
            {
                "heading": "3. DAG Representation for Basic Blocks",
                "highlight": False,
                "content": [
                    "• Leaves: Identifiers or constants with initial values.",
                    "• Interior nodes: Operator symbols labeled with variable names that receive the result.",
                    "• Automatically detects common subexpressions across the basic block."
                ]
            }
        ],
        exam_tip="Clearly distinguish Register Allocation (which variables) vs Assignment (which register).\nExplain Register & Address descriptors to guarantee full 10 marks!"
    )

# ==============================================================================
# 4. CD Module 6 - Topic 1: Principal Sources of Optimization
# ==============================================================================
def render_cd_m6_optimizations():
    v_path = "f:/kachara/project final year/exam_study/compiler_design/cd_m6_optimizations_visual.jpg"
    n_path = "f:/kachara/project final year/exam_study/compiler_design/cd_m6_optimizations_notes.jpg"

    img = Image.new("RGB", (1600, 1000), (15, 23, 42))
    draw = ImageDraw.Draw(img)
    fonts = {
        "title": ImageFont.truetype(FONT_TITLE, 36),
        "sub": ImageFont.truetype(FONT_BODY, 22),
        "card_title": ImageFont.truetype(FONT_TITLE, 24),
        "data": ImageFont.truetype(FONT_CODE, 19),
        "body": ImageFont.truetype(FONT_BODY, 19)
    }

    draw.text((60, 30), "COMPILER DESIGN: PRINCIPAL SOURCES OF OPTIMIZATION (MODULE 6)", fill=(255, 255, 255), font=fonts["title"])
    draw.text((60, 78), "Machine-Independent transformations that preserve program semantics while drastically boosting speed.", fill=(56, 189, 248), font=fonts["sub"])

    cards = [
        {
            "title": "1. FUNCTION-PRESERVING",
            "subtitle": "Local & Global Redundancy",
            "color": (59, 130, 246),
            "lines": [
                ("1. Common Subexpression Elimination:", "Avoid re-computing values already evaluated. e.g., t1 = 4*i; t2 = a[t1]; t3 = 4*i -> reuse t1!"),
                ("", ""),
                ("2. Copy Propagation:", "If x = y, substitute y in place of x in subsequent expressions until x is reassigned."),
                ("", ""),
                ("3. Dead-Code Elimination:", "Remove code whose results are NEVER used (e.g. if (0) { ... }).")
            ]
        },
        {
            "title": "2. LOOP OPTIMIZATIONS",
            "subtitle": "90% of Time Spent in 10% Code",
            "color": (16, 185, 129),
            "lines": [
                ("1. Loop-Invariant Code Motion:", "Move computations that produce identical results on every iteration OUTSIDE the loop header!"),
                ("e.g., while (i <= limit - 2) -> move 't = limit - 2' before loop!"),
                ("", ""),
                ("2. Strength Reduction:", "Replace expensive operations with cheaper ones:"),
                ("Replace multiplication 't = i * 4' in a loop with addition 't = t + 4'!")
            ]
        },
        {
            "title": "3. LOOP UNROLLING & JAMMING",
            "subtitle": "Reducing Branch Overheads",
            "color": (245, 158, 11),
            "lines": [
                ("Loop Unrolling:", "Replicate the loop body multiple times to decrease loop counter comparison & branch jump costs."),
                ("", ""),
                ("Loop Jamming (Loop Fusion):", "Combine two loops with identical index bounds into a single loop body."),
                ("", ""),
                ("Induction Variables:", "Variables that change by a constant step on each loop iteration (e.g. i = i + 1).")
            ]
        }
    ]

    for i, c in enumerate(cards):
        make_visual_card(draw, 60 + i * 500, 130, 460, 580, c["color"], c["title"], c["subtitle"], c["lines"], fonts)

    draw.rounded_rectangle([60, 740, 1540, 960], radius=14, fill=(30, 41, 59), outline=(236, 72, 153), width=2)
    draw.text((90, 755), "★ 10-MARK EXAM TABLE: 5 PRINCIPAL SOURCES OF OPTIMIZATION", fill=(244, 114, 182), font=fonts["card_title"])
    draw.text((90, 800), "1. Common Subexpression Elimination: Saves execution time by reusing existing computed expressions.", fill=(255, 255, 255), font=fonts["data"])
    draw.text((90, 840), "2. Copy Propagation: Enables further dead code elimination and constant folding.", fill=(56, 189, 248), font=fonts["data"])
    draw.text((90, 880), "3. Dead-Code Elimination: Reduces program memory footprint and instruction cache misses.", fill=(250, 204, 21), font=fonts["data"])
    draw.text((90, 920), "4. Code Motion: Moves loop-invariants out of loops.  5. Strength Reduction: Replaces expensive '*' with cheaper '+'.", fill=(74, 222, 128), font=fonts["data"])

    img.save(v_path, quality=95)
    print(f"Saved: {v_path}")

    create_handwritten_notebook(
        output_path=n_path,
        title="PRINCIPAL SOURCES OF OPTIMIZATION (10M)",
        sections=[
            {
                "heading": "1. What is Machine-Independent Optimization?",
                "highlight": True,
                "content": [
                    "• Program transformations applied on Intermediate Representation (IR).",
                    "• Goal: Improve running time and reduce code size without altering output semantics.",
                    "• Criterion: Transformation must be semantic-preserving!"
                ]
            },
            {
                "heading": "2. The 5 Core Optimization Techniques",
                "highlight": True,
                "content": [
                    "1. Common Subexpression Elimination: If an expression E was previously computed",
                    "   and its operands have not changed, reuse the previous evaluation.",
                    "2. Copy Propagation: Use of y for x in x = y allows propagating constants.",
                    "3. Dead Code Elimination: Deleting statements that compute values never referenced.",
                    "4. Loop Invariant Code Motion (Hoisting): Move computations independent of loop index",
                    "   outside the loop to the pre-header.",
                    "5. Strength Reduction: Replace heavy operations (*, /) with lighter ones (+, -)."
                ]
            },
            {
                "heading": "3. Loop Optimization Details",
                "highlight": False,
                "content": [
                    "• Induction Variables: Variables x whose value changes by constant c on each iteration.",
                    "• Reduction in strength: If t = i * 4, replace with t = t + 4 inside the loop!"
                ]
            }
        ],
        exam_tip="Write each of the 5 optimizations with a before/after code snippet\nto guarantee full 10 marks!"
    )

# ==============================================================================
# 5. CD Module 6 - Topic 2: Data-Flow Analysis
# ==============================================================================
def render_cd_m6_dataflow():
    v_path = "f:/kachara/project final year/exam_study/compiler_design/cd_m6_dataflow_visual.jpg"
    n_path = "f:/kachara/project final year/exam_study/compiler_design/cd_m6_dataflow_notes.jpg"

    img = Image.new("RGB", (1600, 1000), (15, 23, 42))
    draw = ImageDraw.Draw(img)
    fonts = {
        "title": ImageFont.truetype(FONT_TITLE, 36),
        "sub": ImageFont.truetype(FONT_BODY, 22),
        "card_title": ImageFont.truetype(FONT_TITLE, 24),
        "data": ImageFont.truetype(FONT_CODE, 19),
        "body": ImageFont.truetype(FONT_BODY, 19)
    }

    draw.text((60, 30), "COMPILER DESIGN: DATA-FLOW ANALYSIS (MODULE 6)", fill=(255, 255, 255), font=fonts["title"])
    draw.text((60, 78), "How the compiler reasons about the flow of values across basic blocks using Transfer Equations.", fill=(56, 189, 248), font=fonts["sub"])

    cards = [
        {
            "title": "1. REACHING DEFINITIONS",
            "subtitle": "Forward Data-Flow Problem",
            "color": (59, 130, 246),
            "lines": [
                ("Question:", "Which variable definitions d: x = ... can REACH program point p without being killed?"),
                ("", ""),
                ("Transfer Equation:", "OUT[B] = gen[B] ∪ ( IN[B] - kill[B] )"),
                ("", ""),
                ("Confluence Operator:", "IN[B] = ∪_(P in pred(B)) OUT[P]  (Union)"),
                ("", ""),
                ("Application:", "Detecting uninitialized variables and constant propagation.")
            ]
        },
        {
            "title": "2. AVAILABLE EXPRESSIONS",
            "subtitle": "Forward, Intersection Problem",
            "color": (16, 185, 129),
            "lines": [
                ("Question:", "Has expression x op y ALREADY been evaluated on ALL paths leading to point p?"),
                ("", ""),
                ("Transfer Equation:", "OUT[B] = e_gen[B] ∪ ( IN[B] - e_kill[B] )"),
                ("", ""),
                ("Confluence Operator:", "IN[B] = ∩_(P in pred(B)) OUT[P]  (INTERSECTION!)"),
                ("", ""),
                ("Application:", "Eliminating Global Common Subexpressions!")
            ]
        },
        {
            "title": "3. LIVE VARIABLE ANALYSIS",
            "subtitle": "BACKWARD Data-Flow Problem",
            "color": (245, 158, 11),
            "lines": [
                ("Question:", "Will the current value of variable x be READ in the future before being reassigned?"),
                ("", ""),
                ("Flow Direction:", "BACKWARD from program exit to entry!"),
                ("", ""),
                ("Transfer Equation:", "IN[B] = use[B] ∪ ( OUT[B] - def[B] )"),
                ("", ""),
                ("Confluence Operator:", "OUT[B] = ∪_(S in succ(B)) IN[S]"),
                ("Application: Register allocation & dead variable cleanup.")
            ]
        }
    ]

    for i, c in enumerate(cards):
        make_visual_card(draw, 60 + i * 500, 130, 460, 580, c["color"], c["title"], c["subtitle"], c["lines"], fonts)

    draw.rounded_rectangle([60, 740, 1540, 960], radius=14, fill=(30, 41, 59), outline=(99, 102, 241), width=2)
    draw.text((90, 755), "★ MASTER EXAM MATRIX: 3 CLASSIC DATA-FLOW SCHEMAS (10 MARKS)", fill=(165, 180, 252), font=fonts["card_title"])
    draw.text((90, 800), "• Reaching Definitions: Forward flow | Confluence = Union (∪) | Init: OUT[B] = Empty | gen/kill framework.", fill=(255, 255, 255), font=fonts["data"])
    draw.text((90, 840), "• Available Expressions: Forward flow | Confluence = Intersection (∩) | Init: OUT[B] = All expressions | e_gen/e_kill.", fill=(56, 189, 248), font=fonts["data"])
    draw.text((90, 880), "• Live Variables: Backward flow | Confluence = Union (∪) | Init: IN[B] = Empty | use/def framework.", fill=(250, 204, 21), font=fonts["data"])
    draw.text((90, 920), "General Data-Flow Framework: Semi-lattice (L, ∧), Transfer functions f_B: L -> L. Fixed-point iteration converges!", fill=(74, 222, 128), font=fonts["data"])

    img.save(v_path, quality=95)
    print(f"Saved: {v_path}")

    create_handwritten_notebook(
        output_path=n_path,
        title="DATA-FLOW ANALYSIS (10 MARKS)",
        sections=[
            {
                "heading": "1. What is Data-Flow Analysis?",
                "highlight": True,
                "content": [
                    "• Technique to gather information about the possible set of runtime values",
                    "  at various points in a program's Control Flow Graph (CFG).",
                    "• Uses iterative data-flow equations until a fixed point is reached."
                ]
            },
            {
                "heading": "2. Three Major Data-Flow Problems (Must Compare in Exam!)",
                "highlight": True,
                "content": [
                    "1. Reaching Definitions (Forward, Union):",
                    "   OUT[B] = gen[B] union (IN[B] - kill[B]), where IN[B] = union OUT[P].",
                    "2. Available Expressions (Forward, Intersection):",
                    "   OUT[B] = e_gen[B] union (IN[B] - e_kill[B]), where IN[B] = intersection OUT[P].",
                    "3. Live Variables (Backward, Union):",
                    "   IN[B] = use[B] union (OUT[B] - def[B]), where OUT[B] = union IN[S]."
                ]
            },
            {
                "heading": "3. Foundations of Data-Flow Analysis",
                "highlight": False,
                "content": [
                    "• Meet operator (confluence) defines information combination (union vs intersection).",
                    "• Transfer function f_B models state transformation by basic block B.",
                    "• Monotonicity guarantees termination of iterative fixed-point algorithm."
                ]
            }
        ],
        exam_tip="Always write the IN/OUT equations for all 3 schemas and specify direction\n(Forward vs Backward) and meet operator (Union vs Intersection) for full 10 marks!"
    )

if __name__ == "__main__":
    print("Generating CD Module 5 Topic 1 (Runtime & Storage)...")
    render_cd_m5_runtime()
    print("Generating CD Module 5 Topic 2 (Basic Blocks & Flow Graphs)...")
    render_cd_m5_basic_blocks()
    print("Generating CD Module 5 Topic 3 (Code Generation & Registers)...")
    render_cd_m5_codegen()
    print("Generating CD Module 6 Topic 1 (Optimizations)...")
    render_cd_m6_optimizations()
    print("Generating CD Module 6 Topic 2 (Data-Flow Analysis)...")
    render_cd_m6_dataflow()
    print("All Compiler Design Modules 5 and 6 rendered successfully!")
