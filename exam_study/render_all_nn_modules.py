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
                lbl, val = "", item[0]
            else:
                lbl, val = item[0], item[1]
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
# 1. NN Module 4 - Topic 4: Virtues, Limitations & Momentum
# ==============================================================================
def render_nn_m4_momentum():
    v_path = "f:/kachara/project final year/exam_study/neural_networks/nn_m4_momentum_visual.jpg"
    n_path = "f:/kachara/project final year/exam_study/neural_networks/nn_m4_momentum_notes.jpg"

    img = Image.new("RGB", (1600, 1000), (15, 23, 42))
    draw = ImageDraw.Draw(img)
    fonts = {
        "title": ImageFont.truetype(FONT_TITLE, 36),
        "sub": ImageFont.truetype(FONT_BODY, 22),
        "card_title": ImageFont.truetype(FONT_TITLE, 24),
        "data": ImageFont.truetype(FONT_CODE, 19),
        "body": ImageFont.truetype(FONT_BODY, 19)
    }

    draw.text((60, 30), "NEURAL NETWORKS: VIRTUES, LIMITATIONS & ACCELERATED CONVERGENCE (MOMENTUM)", fill=(255, 255, 255), font=fonts["title"])
    draw.text((60, 78), "How backprop works well, where it gets trapped, and how adding momentum speeds up training 10x.", fill=(56, 189, 248), font=fonts["sub"])

    cards = [
        {
            "title": "1. VIRTUES OF BACKPROP",
            "subtitle": "Why Backprop Revolutionized AI",
            "color": (16, 185, 129),
            "lines": [
                ("• Universal Approximator:", "Can approximate any continuous non-linear function with 1 hidden layer."),
                ("", ""),
                ("• Efficient Gradient:", "Chain rule scales linearly O(W) with number of weights instead of exponential."),
                ("", ""),
                ("• Local Computation:", "Each neuron only needs signals from adjacent connected layers.")
            ]
        },
        {
            "title": "2. MAJOR LIMITATIONS",
            "subtitle": "Where Standard Backprop Fails",
            "color": (239, 68, 68),
            "lines": [
                ("• Local Minima Trap:", "Network can get stuck in a bad local dip rather than global minimum."),
                ("", ""),
                ("• Vanishing Gradients:", "Sigmoid derivative is max 0.25; gradients shrink to zero in deep layers."),
                ("", ""),
                ("• Slow Convergence:", "In flat plateau areas, step size shrinks to near zero, taking thousands of epochs.")
            ]
        },
        {
            "title": "3. MOMENTUM ACCELERATION",
            "subtitle": "Heavy Ball Rolling Down Hill",
            "color": (245, 158, 11),
            "lines": [
                ("The Concept:", "Add a fraction alpha of the previous step to the current update."),
                ("", ""),
                ("• Cancels Oscillations:", "Sideways bouncing across steep walls cancels out!"),
                ("", ""),
                ("• Accelerates Down Valley:", "Consistent forward motion builds velocity like a heavy snowball."),
                ("", ""),
                ("• Escapes Small Dips:", "Momentum carries the weights over shallow local traps.")
            ]
        }
    ]

    for i, c in enumerate(cards):
        make_visual_card(draw, 60 + i * 500, 130, 460, 580, c["color"], c["title"], c["subtitle"], c["lines"], fonts)

    # Bottom Formula
    draw.rounded_rectangle([60, 740, 1540, 960], radius=14, fill=(30, 41, 59), outline=(16, 185, 129), width=2)
    draw.text((90, 755), "★ 10-MARK EXAM FORMULA: WEIGHT UPDATE WITH MOMENTUM CONSTANT", fill=(110, 231, 183), font=fonts["card_title"])
    draw.text((90, 800), "Formula:  Δw(n) = α * Δw(n-1) + η * δ(n) * y(n)", fill=(250, 204, 21), font=fonts["data"])
    draw.text((90, 840), "Where: α = Momentum factor (typically 0.9), η = Learning rate, δ = Local gradient, y = Input/activation.", fill=(255, 255, 255), font=fonts["data"])
    draw.text((90, 880), "Physical Analogy: Mass of heavy ball gives it inertia, smoothing zig-zag paths and speeding convergence.", fill=(56, 189, 248), font=fonts["data"])
    draw.text((90, 920), "Delta-Bar-Delta Rule: Adaptive heuristic that increases learning rate when consecutive gradients agree.", fill=(248, 113, 113), font=fonts["data"])

    img.save(v_path, quality=95)
    print(f"Saved: {v_path}")

    create_handwritten_notebook(
        output_path=n_path,
        title="VIRTUES, LIMITATIONS & MOMENTUM (10M)",
        sections=[
            {
                "heading": "1. Virtues (Strengths) of Backpropagation",
                "highlight": True,
                "content": [
                    "• Universal Function Approximation (Cybenko theorem).",
                    "• Computational efficiency: O(W) complexity per sample via dynamic programming.",
                    "• Parallel distributed processing nature.",
                    "• Self-learning capability directly from raw input-output examples."
                ]
            },
            {
                "heading": "2. Limitations & Pitfalls",
                "highlight": False,
                "content": [
                    "• Susceptible to local minima & saddle points.",
                    "• Vanishing Gradient problem: f'(net) for sigmoid peaks at 0.25, fading across layers.",
                    "• Flat plateau regions cause painfully slow learning.",
                    "• Choice of learning rate eta is critical (too small = slow, too big = divergence)."
                ]
            },
            {
                "heading": "3. Accelerated Convergence: Momentum Method",
                "highlight": True,
                "content": [
                    "• Formula: Delta w(n) = alpha * Delta w(n-1) + eta * delta(n) * y(n)",
                    "• alpha is momentum constant (0 <= alpha < 1, usually 0.9).",
                    "• Acting as a low-pass filter: suppresses high-frequency zig-zag oscillations,",
                    "  while reinforcing low-frequency consistent downward motion."
                ]
            },
            {
                "heading": "4. Heuristic: Delta-Bar-Delta",
                "highlight": False,
                "content": [
                    "• Each weight has its own independent learning rate eta_k.",
                    "• If sign of gradient dE/dw remains unchanged -> increase eta_k linearly.",
                    "• If sign of gradient alternates -> decrease eta_k exponentially!"
                ]
            }
        ],
        exam_tip="Always write the momentum formula Delta w(n) = alpha*Delta w(n-1) + eta*delta*y\nand list 3 Virtues and 3 Limitations for full 10 marks!"
    )

# ==============================================================================
# 2. NN Module 5 - Topic 1: Self-Organizing Maps (SOM) Algorithm
# ==============================================================================
def render_nn_m5_som():
    v_path = "f:/kachara/project final year/exam_study/neural_networks/nn_m5_som_visual.jpg"
    n_path = "f:/kachara/project final year/exam_study/neural_networks/nn_m5_som_notes.jpg"

    img = Image.new("RGB", (1600, 1000), (15, 23, 42))
    draw = ImageDraw.Draw(img)
    fonts = {
        "title": ImageFont.truetype(FONT_TITLE, 36),
        "sub": ImageFont.truetype(FONT_BODY, 22),
        "card_title": ImageFont.truetype(FONT_TITLE, 24),
        "data": ImageFont.truetype(FONT_CODE, 19),
        "body": ImageFont.truetype(FONT_BODY, 19)
    }

    draw.text((60, 30), "NEURAL NETWORKS: SELF-ORGANIZING MAPS (SOM) — TEUVO KOHONEN", fill=(255, 255, 255), font=fonts["title"])
    draw.text((60, 78), "Module 5: Unsupervised Competitive Learning that maps high-dimensional data onto a 2D topographic grid.", fill=(56, 189, 248), font=fonts["sub"])

    cards = [
        {
            "title": "PHASE 1: COMPETITION",
            "subtitle": "Finding the Best Matching Unit (BMU)",
            "color": (59, 130, 246),
            "lines": [
                ("The Contest:", "All output neurons compete for ownership of input vector x."),
                ("", ""),
                ("Metric:", "Euclidean distance ||x - w_j|| between input x and weight vector w_j."),
                ("", ""),
                ("Winner (BMU) i(x):", "The neuron with the SMALLEST distance:"),
                ("Formula:", "i(x) = argmin_j || x - w_j ||"),
                ("", ""),
                ("Result:", "Only the BMU and its neighbors get to learn!")
            ]
        },
        {
            "title": "PHASE 2: COOPERATION",
            "subtitle": "Topological Neighborhood",
            "color": (16, 185, 129),
            "lines": [
                ("Lateral Interaction:", "The winning neuron excites its immediate neighbors in the 2D lattice."),
                ("", ""),
                ("Gaussian Function:", "h_j,i(x)(t) = exp( - d_ji^2 / (2 * sigma(t)^2) )"),
                ("", ""),
                ("Properties:", "• Maximum (1.0) at winner neuron."),
                ("• Decays smoothly to 0 with distance."),
                ("• Neighborhood radius sigma(t) shrinks over time!")
            ]
        },
        {
            "title": "PHASE 3: ADAPTATION",
            "subtitle": "Synaptic Weight Update",
            "color": (236, 72, 153),
            "lines": [
                ("Weight Adjustment:", "Pull the weights of BMU and neighbors closer to input x."),
                ("", ""),
                ("Update Rule:", "w_j(t+1) = w_j(t) + eta(t) * h_j,i(t) * [ x - w_j(t) ]"),
                ("", ""),
                ("Two Key Stages:", "1. Ordering Phase: Large neighborhood & learning rate; establishes rough topology."),
                ("2. Convergence Phase: Tiny radius & rate; fine-tunes coordinates.")
            ]
        }
    ]

    for i, c in enumerate(cards):
        make_visual_card(draw, 60 + i * 500, 130, 460, 580, c["color"], c["title"], c["subtitle"], c["lines"], fonts)

    draw.rounded_rectangle([60, 740, 1540, 960], radius=14, fill=(30, 41, 59), outline=(99, 102, 241), width=2)
    draw.text((90, 755), "★ EXAM SUMMARY: 2 CORE PROPERTIES OF FEATURE MAPS (5 MARKS)", fill=(165, 180, 252), font=fonts["card_title"])
    draw.text((90, 800), "1. Approximation of Input Space: The weight vectors w_j form a representative sample of input space distribution p(x).", fill=(255, 255, 255), font=fonts["data"])
    draw.text((90, 840), "2. Topological Ordering: If two input vectors x1 and x2 are close in high-D space, their BMUs will be close on 2D grid!", fill=(56, 189, 248), font=fonts["data"])
    draw.text((90, 880), "Two Basic Models: 1. Willshaw-von der Malsburg model (Biological retino-tectal map). 2. Kohonen SOM (Abstract engineering algorithm).", fill=(250, 204, 21), font=fonts["data"])
    draw.text((90, 920), "Contextual Maps & Hierarchical VQ: Decomposes complex spaces into hierarchical clusters (tree of smaller SOMs).", fill=(74, 222, 128), font=fonts["data"])

    img.save(v_path, quality=95)
    print(f"Saved: {v_path}")

    create_handwritten_notebook(
        output_path=n_path,
        title="SELF-ORGANIZING MAPS (SOM) (10 MARKS)",
        sections=[
            {
                "heading": "1. What is Kohonen's SOM?",
                "highlight": True,
                "content": [
                    "• Unsupervised neural network that converts high-dimensional complex input spaces",
                    "  into discrete 1D or 2D topological map while preserving metric relationships.",
                    "• Inspired by sensory cortex of human brain (tonotopic, retinotopic organization)."
                ]
            },
            {
                "heading": "2. The 3 Essential Processes of SOM",
                "highlight": True,
                "content": [
                    "1. Competition: Each neuron computes discriminant function d_j(x) = ||x - w_j||.",
                    "   BMU winner i(x) = argmin_j ||x - w_j||.",
                    "2. Cooperation: Neighborhood function h_j,i(t) = exp(-d_ji^2 / (2*sigma(t)^2)).",
                    "   Neighborhood shrinks with time: sigma(t) = sigma_0 * exp(-t / tau_1).",
                    "3. Adaptation: w_j(t+1) = w_j(t) + eta(t) * h_j,i(t) * [x - w_j(t)]."
                ]
            },
            {
                "heading": "3. Two Basic Feature Mapping Models",
                "highlight": False,
                "content": [
                    "• Willshaw-von der Malsburg Model: Biologically motivated; maps retina to cortex",
                    "  using lateral inhibition & synaptic chemical markers.",
                    "• Kohonen Model: Computationally efficient; uses algorithmic topological neighborhoods."
                ]
            },
            {
                "heading": "4. Properties of the Feature Map",
                "highlight": False,
                "content": [
                    "• Dimension Reduction: Preserves spatial relationships from R^n to 2D grid.",
                    "• Optimal Vector Quantization: Clusters high density regions with more neurons.",
                    "• Feature Coordination: Coordinates multiple input features smoothly across map."
                ]
            }
        ],
        exam_tip="Always write the 3 phases: Competition (argmin), Cooperation (Gaussian h_ji), and\nAdaptation (w(t+1) formula) to secure full 10 marks!"
    )

# ==============================================================================
# 3. NN Module 5 - Topic 2: LVQ & Kernel SOM
# ==============================================================================
def render_nn_m5_lvq():
    v_path = "f:/kachara/project final year/exam_study/neural_networks/nn_m5_lvq_visual.jpg"
    n_path = "f:/kachara/project final year/exam_study/neural_networks/nn_m5_lvq_notes.jpg"

    img = Image.new("RGB", (1600, 1000), (15, 23, 42))
    draw = ImageDraw.Draw(img)
    fonts = {
        "title": ImageFont.truetype(FONT_TITLE, 36),
        "sub": ImageFont.truetype(FONT_BODY, 22),
        "card_title": ImageFont.truetype(FONT_TITLE, 24),
        "data": ImageFont.truetype(FONT_CODE, 19),
        "body": ImageFont.truetype(FONT_BODY, 19)
    }

    draw.text((60, 30), "NEURAL NETWORKS: LEARNING VECTOR QUANTIZATION (LVQ) & KERNEL SOM", fill=(255, 255, 255), font=fonts["title"])
    draw.text((60, 78), "Supervised classification using competitive prototype vectors and non-linear Kernel mappings.", fill=(56, 189, 248), font=fonts["sub"])

    cards = [
        {
            "title": "1. WHAT IS LVQ?",
            "subtitle": "Supervised Competitive Learning",
            "color": (59, 130, 246),
            "lines": [
                ("Purpose:", "Unlike SOM (unsupervised), LVQ is SUPERVISED for classification."),
                ("", ""),
                ("Architecture:", "A set of prototype / codebook vectors w_j, each assigned a class label."),
                ("", ""),
                ("Classification:", "Given input x, find closest prototype w_c. Predict label of w_c."),
                ("", ""),
                ("Analogy:", "Each class sends a representative. You vote for the representative closest to you!")
            ]
        },
        {
            "title": "2. LVQ LEARNING RULES",
            "subtitle": "Reward (Pull) vs Penalty (Push)",
            "color": (16, 185, 129),
            "lines": [
                ("Find Closest:", "w_c = argmin_j || x - w_j ||"),
                ("", ""),
                ("CASE A: CORRECT CLASS (Reward)", "w_c(t+1) = w_c(t) + eta * [ x - w_c(t) ]"),
                ("-> PULLS prototype closer to input!"),
                ("", ""),
                ("CASE B: WRONG CLASS (Penalty)", "w_c(t+1) = w_c(t) - eta * [ x - w_c(t) ]"),
                ("-> PUSHES prototype away from input!")
            ]
        },
        {
            "title": "3. KERNEL SOM & KL DIVERGENCE",
            "subtitle": "Non-linear Space Mapping",
            "color": (245, 158, 11),
            "lines": [
                ("Kernel SOM:", "Maps inputs x into high-D feature space via Kernel function k(x, y)."),
                ("", ""),
                ("Why?", "Enables discovering highly non-linear clusters that standard Euclidean SOM misses."),
                ("", ""),
                ("Kullback-Leibler (KL) Divergence:", "Measures relative entropy between true distribution P(x) and map model Q(x)."),
                ("", ""),
                ("Minimizing KL Divergence:", "Proves SOM asymptotically maximizes mutual information!")
            ]
        }
    ]

    for i, c in enumerate(cards):
        make_visual_card(draw, 60 + i * 500, 130, 460, 580, c["color"], c["title"], c["subtitle"], c["lines"], fonts)

    draw.rounded_rectangle([60, 740, 1540, 960], radius=14, fill=(30, 41, 59), outline=(236, 72, 153), width=2)
    draw.text((90, 755), "★ 5-MARK EXAM COMPARISON: SOM (UNSUPERVISED) vs LVQ (SUPERVISED)", fill=(244, 114, 182), font=fonts["card_title"])
    draw.text((90, 800), "• Supervision: SOM is Unsupervised (no class labels) vs LVQ is Supervised (uses class labels).", fill=(255, 255, 255), font=fonts["data"])
    draw.text((90, 840), "• Objective: SOM preserves topology & reduces dimension vs LVQ defines optimal classification decision boundaries.", fill=(56, 189, 248), font=fonts["data"])
    draw.text((90, 880), "• Update rule: SOM updates winner & all neighbors vs LVQ updates ONLY the winning prototype (pull or push).", fill=(250, 204, 21), font=fonts["data"])
    draw.text((90, 920), "• LVQ2 / LVQ3 Extensions: Updates two closest prototypes if input falls in the boundary margin window.", fill=(74, 222, 128), font=fonts["data"])

    img.save(v_path, quality=95)
    print(f"Saved: {v_path}")

    create_handwritten_notebook(
        output_path=n_path,
        title="LVQ & KERNEL SOM (10 MARKS)",
        sections=[
            {
                "heading": "1. Learning Vector Quantization (LVQ)",
                "highlight": True,
                "content": [
                    "• Supervised competitive learning algorithm designed by Kohonen for pattern classification.",
                    "• Uses labeled prototype vectors (codebook vectors) to define Voronoi tessellation.",
                    "• Approximates Bayes optimal decision boundary directly from training data."
                ]
            },
            {
                "heading": "2. LVQ1 Learning Algorithm",
                "highlight": True,
                "content": [
                    "1. For input x with class C_x, find closest codebook vector w_c:",
                    "   ||x - w_c|| = min_j ||x - w_j||",
                    "2. If Class(w_c) == C_x (Correct):",
                    "   w_c(t+1) = w_c(t) + eta(t) * [x - w_c(t)]  (Attraction / Pull)",
                    "3. If Class(w_c) != C_x (Wrong):",
                    "   w_c(t+1) = w_c(t) - eta(t) * [x - w_c(t)]  (Repulsion / Push)",
                    "4. Other codebook vectors (j != c) remain unchanged."
                ]
            },
            {
                "heading": "3. Kernel SOM & KL Divergence",
                "highlight": False,
                "content": [
                    "• Kernel trick: Implicitly maps data into reproducing kernel Hilbert space (RKHS).",
                    "• Distance metric: d^2(x, w) = k(x, x) - 2*k(x, w) + k(w, w).",
                    "• Kullback-Leibler (KL) Divergence: D_KL(P || Q) = sum P(x) log(P(x)/Q(x)).",
                    "  Shows SOM acts as maximum entropy estimator of input density."
                ]
            }
        ],
        exam_tip="Write both cases (+eta pull for correct class, -eta push for incorrect class).\nDraw the 3-point comparison table between SOM and LVQ for full marks!"
    )

# ==============================================================================
# 4. NN Module 6 - Topic 1: Neuro Dynamics, Attractors & Hopfield Networks
# ==============================================================================
def render_nn_m6_hopfield():
    v_path = "f:/kachara/project final year/exam_study/neural_networks/nn_m6_hopfield_visual.jpg"
    n_path = "f:/kachara/project final year/exam_study/neural_networks/nn_m6_hopfield_notes.jpg"

    img = Image.new("RGB", (1600, 1000), (15, 23, 42))
    draw = ImageDraw.Draw(img)
    fonts = {
        "title": ImageFont.truetype(FONT_TITLE, 36),
        "sub": ImageFont.truetype(FONT_BODY, 22),
        "card_title": ImageFont.truetype(FONT_TITLE, 24),
        "data": ImageFont.truetype(FONT_CODE, 19),
        "body": ImageFont.truetype(FONT_BODY, 19)
    }

    draw.text((60, 30), "NEURAL NETWORKS: NEURO DYNAMICS, ATTRACTORS & HOPFIELD MODELS", fill=(255, 255, 255), font=fonts["title"])
    draw.text((60, 78), "Module 6: Recurrent dynamical systems that store associative memories as energy minima attractors.", fill=(56, 189, 248), font=fonts["sub"])

    cards = [
        {
            "title": "1. DYNAMICAL SYSTEMS",
            "subtitle": "Stability & Lyapunov Function",
            "color": (59, 130, 246),
            "lines": [
                ("State Trajectory:", "Network state evolves over time: x(t+1) = f(W * x(t))."),
                ("", ""),
                ("Lyapunov Energy Function:", "A scalar function E(x) that MUST strictly decrease or remain constant: dE/dt <= 0."),
                ("", ""),
                ("Equilibrium State:", "The system naturally rolls downhill into energy valley and freezes (stable fixed point)."),
                ("", ""),
                ("Guaranteed Stability:", "Prevents chaotic oscillations or infinite loops!")
            ]
        },
        {
            "title": "2. ATTRACTORS PARADIGM",
            "subtitle": "Associative Memory Basin",
            "color": (16, 185, 129),
            "lines": [
                ("What is an Attractor?", "A stable state toward which nearby trajectories are drawn."),
                ("", ""),
                ("Types of Attractors:", "• Point Attractor: Settles to a single memory state."),
                ("• Limit Cycle: Periodic oscillation."),
                ("• Strange Attractor: Chaotic trajectory."),
                ("", ""),
                ("Content-Addressable Memory:", "Feed a noisy/incomplete image -> Network state falls into the attractor basin and reconstructs the clean original!")
            ]
        },
        {
            "title": "3. HOPFIELD NETWORK",
            "subtitle": "Discrete Hopfield Model",
            "color": (245, 158, 11),
            "lines": [
                ("Architecture:", "Single layer, fully connected, RECURRENT network."),
                ("", ""),
                ("Symmetric Weights:", "w_ij = w_ji  AND  w_ii = 0 (no self-loops)."),
                ("", ""),
                ("Binary/Bipolar States:", "s_i in { +1, -1 }."),
                ("", ""),
                ("Hebbian Learning Rule:", "W = (1/N) * sum_mu (xi^mu * (xi^mu)^T)"),
                ("", ""),
                ("Storage Capacity:", "P_max ≈ 0.138 * N  (N neurons can store ~0.14N patterns).")
            ]
        }
    ]

    for i, c in enumerate(cards):
        make_visual_card(draw, 60 + i * 500, 130, 460, 580, c["color"], c["title"], c["subtitle"], c["lines"], fonts)

    draw.rounded_rectangle([60, 740, 1540, 960], radius=14, fill=(30, 41, 59), outline=(16, 185, 129), width=2)
    draw.text((90, 755), "★ EXAM CORE FORMULAS: HOPFIELD ENERGY FUNCTION & ASYNCHRONOUS UPDATE", fill=(110, 231, 183), font=fonts["card_title"])
    draw.text((90, 800), "Hopfield Energy:  E = - (1/2) * sum_i sum_j (w_ij * s_i * s_j) - sum_i (theta_i * s_i)", fill=(250, 204, 21), font=fonts["data"])
    draw.text((90, 840), "Neuron Update Rule:  s_i(t+1) = sgn( sum_j (w_ij * s_j) - theta_i )", fill=(255, 255, 255), font=fonts["data"])
    draw.text((90, 880), "Energy Monotonicity Proof:  Delta E = - Delta s_i * [ sum_j (w_ij * s_j) - theta_i ] <= 0  (Always decreases!)", fill=(56, 189, 248), font=fonts["data"])
    draw.text((90, 920), "Spurious States: Unwanted false energy dips created by Hebbian crosstalk (solved by Boltzmann machines).", fill=(248, 113, 113), font=fonts["data"])

    img.save(v_path, quality=95)
    print(f"Saved: {v_path}")

    create_handwritten_notebook(
        output_path=n_path,
        title="HOPFIELD NETWORKS & ATTRACTORS (10M)",
        sections=[
            {
                "heading": "1. What is Neuro Dynamics?",
                "highlight": True,
                "content": [
                    "• Studies time-evolution of neural activity in recurrent feedback networks.",
                    "• Described by differential equations (continuous) or difference equations (discrete).",
                    "• Attractor: Region in state space that pulls surrounding states into it.",
                    "• Content-Addressable Memory (CAM): Retrieves stored memories from corrupted cues."
                ]
            },
            {
                "heading": "2. Discrete Hopfield Network Architecture",
                "highlight": False,
                "content": [
                    "• Fully connected recurrent network with bipolar neurons s_i in {-1, +1}.",
                    "• Symmetric connection weights: w_ij = w_ji.",
                    "• Zero diagonal elements: w_ii = 0 (no self-feedback).",
                    "• Asynchronous state update: Pick one neuron i at random, update state s_i."
                ]
            },
            {
                "heading": "3. Lyapunov Energy Function & Convergence",
                "highlight": True,
                "content": [
                    "• Energy E = - 0.5 * sum_i sum_j (w_ij * s_i * s_j) + sum_i (theta_i * s_i).",
                    "• John Hopfield proved that every asynchronous update ensures Delta E <= 0.",
                    "• Since E is bounded below, network is mathematically guaranteed to reach stable equilibrium!"
                ]
            },
            {
                "heading": "4. Storage Capacity & Spurious States",
                "highlight": False,
                "content": [
                    "• Hebbian storage: w_ij = (1/N) * sum_mu (xi_i^mu * xi_j^mu).",
                    "• Maximum theoretical storage capacity: P_max = 0.138 * N patterns.",
                    "• Spurious States: False local minima (inverted states, mixtures) that trap memory."
                ]
            }
        ],
        exam_tip="State the 2 structural rules (w_ij = w_ji, w_ii = 0), write the Lyapunov Energy equation,\nand show that Delta E <= 0 to score 10/10!"
    )

# ==============================================================================
# 5. NN Module 6 - Topic 2: Restricted Boltzmann Machine (RBM)
# ==============================================================================
def render_nn_m6_rbm():
    v_path = "f:/kachara/project final year/exam_study/neural_networks/nn_m6_rbm_visual.jpg"
    n_path = "f:/kachara/project final year/exam_study/neural_networks/nn_m6_rbm_notes.jpg"

    img = Image.new("RGB", (1600, 1000), (15, 23, 42))
    draw = ImageDraw.Draw(img)
    fonts = {
        "title": ImageFont.truetype(FONT_TITLE, 36),
        "sub": ImageFont.truetype(FONT_BODY, 22),
        "card_title": ImageFont.truetype(FONT_TITLE, 24),
        "data": ImageFont.truetype(FONT_CODE, 19),
        "body": ImageFont.truetype(FONT_BODY, 19)
    }

    draw.text((60, 30), "NEURAL NETWORKS: RESTRICTED BOLTZMANN MACHINE (RBM)", fill=(255, 255, 255), font=fonts["title"])
    draw.text((60, 78), "Module 6: Energy-based probabilistic generative model that forms the building block of Deep Belief Nets.", fill=(56, 189, 248), font=fonts["sub"])

    cards = [
        {
            "title": "1. BIPARTITE ARCHITECTURE",
            "subtitle": "Why 'Restricted'?",
            "color": (59, 130, 246),
            "lines": [
                ("Two Layers:", "• Visible Layer v (observed data features)."),
                ("• Hidden Layer h (latent abstract representations)."),
                ("", ""),
                ("The 'Restricted' Rule:", "NO intra-layer connections allowed!"),
                ("• No visible-to-visible links."),
                ("• No hidden-to-hidden links."),
                ("", ""),
                ("Massive Advantage:", "All hidden units are conditionally INDEPENDENT given visible units! Enables parallel Gibbs sampling.")
            ]
        },
        {
            "title": "2. ENERGY & PROBABILITY",
            "subtitle": "Boltzmann Distribution",
            "color": (16, 185, 129),
            "lines": [
                ("Energy Function E(v, h):", "E(v, h) = - v^T * W * h - a^T * v - b^T * h"),
                ("Where a = visible bias, b = hidden bias."),
                ("", ""),
                ("Joint Probability:", "P(v, h) = (1 / Z) * exp( - E(v, h) )"),
                ("Where Z = Partition function (sum of all states)."),
                ("", ""),
                ("Conditional Probabilities (Sigmoidal):", "P(h_j = 1 | v) = sigmoid( b_j + sum_i v_i * w_ij )"),
                ("P(v_i = 1 | h) = sigmoid( a_i + sum_j h_j * w_ij )")
            ]
        },
        {
            "title": "3. CONTRASTIVE DIVERGENCE",
            "subtitle": "Fast Training (Geoffrey Hinton)",
            "color": (236, 72, 153),
            "lines": [
                ("The Bottleneck:", "Computing partition function Z takes exponential time 2^(V+H)."),
                ("", ""),
                ("Hinton's CD-k Algorithm:", "1. Positive Phase: Sample h_0 given training data v_0."),
                ("2. Negative Phase: Reconstruct v_1 from h_0, then resample h_1 from v_1."),
                ("", ""),
                ("Weight Update:", "Delta W = eta * [ (v_0 * h_0^T) - (v_k * h_k^T) ]"),
                ("Difference between data reality and dream reconstruction!")
            ]
        }
    ]

    for i, c in enumerate(cards):
        make_visual_card(draw, 60 + i * 500, 130, 460, 580, c["color"], c["title"], c["subtitle"], c["lines"], fonts)

    draw.rounded_rectangle([60, 740, 1540, 960], radius=14, fill=(30, 41, 59), outline=(245, 158, 11), width=2)
    draw.text((90, 755), "★ EXAM CHEAT-SHEET: CONTRASTIVE DIVERGENCE (CD-1) WEIGHT UPDATE", fill=(254, 240, 138), font=fonts["card_title"])
    draw.text((90, 800), "Weight Update:  Δw_ij = η * ( < v_i * h_j >_data - < v_i * h_j >_model )", fill=(250, 204, 21), font=fonts["data"])
    draw.text((90, 840), "Physical Interpretation: Increases probability of training data by lowering its energy, and raises energy of fake hallucinations.", fill=(255, 255, 255), font=fonts["data"])
    draw.text((90, 880), "Stochastic Neurons: State activation is probabilistic: s_i = 1 with probability P = 1 / (1 + exp(-net_i / T)).", fill=(56, 189, 248), font=fonts["data"])
    draw.text((90, 920), "Application: Stacked RBMs are trained greedily layer-by-layer to form Deep Belief Networks (DBNs).", fill=(74, 222, 128), font=fonts["data"])

    img.save(v_path, quality=95)
    print(f"Saved: {v_path}")

    create_handwritten_notebook(
        output_path=n_path,
        title="RESTRICTED BOLTZMANN MACHINE (10M)",
        sections=[
            {
                "heading": "1. What is an RBM?",
                "highlight": True,
                "content": [
                    "• A two-layer, stochastic generative neural network with undirected connections.",
                    "• Bipartite graph: Visible layer v and Hidden layer h.",
                    "• 'Restricted': No connections within visible units or within hidden units.",
                    "• Used for unsupervised feature learning, dimensionality reduction, and collaborative filtering."
                ]
            },
            {
                "heading": "2. Energy Function & Probabilities",
                "highlight": False,
                "content": [
                    "• Energy: E(v, h) = - sum_i a_i v_i - sum_j b_j h_j - sum_i sum_j v_i w_ij h_j.",
                    "• Joint probability: P(v, h) = exp(-E(v, h)) / Z  (where Z is partition function).",
                    "• Conditional probabilities are independent factorial sigmoids:",
                    "  P(h_j = 1 | v) = sigma(b_j + sum_i v_i w_ij)",
                    "  P(v_i = 1 | h) = sigma(a_i + sum_j h_j w_ij)"
                ]
            },
            {
                "heading": "3. Contrastive Divergence (CD-k) Training",
                "highlight": True,
                "content": [
                    "• Geoffrey Hinton algorithm avoiding intractable Z partition function.",
                    "• 1. Clamp visible units to training vector v_0, compute P(h_0|v_0).",
                    "• 2. Reconstruct visible units v_1 by sampling from P(v_1|h_0).",
                    "• 3. Resample hidden units h_1 from P(h_1|v_1).",
                    "• Update rule: Delta w_ij = eta * [ (v_0 * h_0) - (v_1 * h_1) ]."
                ]
            }
        ],
        exam_tip="Draw the bipartite graph (visible units at bottom, hidden on top, no horizontal links).\nWrite the energy equation E(v, h) and CD-1 update formula for full 10 marks!"
    )

if __name__ == "__main__":
    print("Generating NN Module 4 Topic 4 (Momentum)...")
    render_nn_m4_momentum()
    print("Generating NN Module 5 Topic 1 (SOM)...")
    render_nn_m5_som()
    print("Generating NN Module 5 Topic 2 (LVQ & Kernel SOM)...")
    render_nn_m5_lvq()
    print("Generating NN Module 6 Topic 1 (Hopfield & Attractors)...")
    render_nn_m6_hopfield()
    print("Generating NN Module 6 Topic 2 (RBM)...")
    render_nn_m6_rbm()
    print("All remaining Neural Networks modules rendered successfully!")
