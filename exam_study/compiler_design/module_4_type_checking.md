# Module 4: Type Checking & Intermediate-Code Generation 📘

## Syllabus Roadmap (RAMRAO ADIK INSTITUTE OF TECHNOLOGY)
1. **Topic 1**: Introduction to Type Checking (Role, Position, I/O)
2. **Topic 2**: Type Systems & Type Expressions (Basic vs Constructed types)
3. **Topic 3**: Specification of a Simple Type Checker (Typing Rules / SDD)
4. **Topic 4**: Equivalence of Type Expressions (Structural vs Name Equivalence)
5. **Topic 5**: Intermediate-Code Generation (Role & Need for Intermediate Representation)
6. **Topic 6**: Intermediate Languages (Syntax Trees, DAGs, Postfix, Three-Address Code)
7. **Topic 7**: Three-Address Code (Quadruples, Triples, Indirect Triples)
8. **Topic 8**: Declarations & Address Calculation (Types & Offset Computation)

## 📖 Jargon Buster (Difficult Words Decoded Before We Start)

| Term | What it Means in Simple English | Real-Life Analogy / Example |
| :--- | :--- | :--- |
| **Syntax** | **Grammar & Structure**. Are words in the right order? | *"Apple eats boy"* has valid English grammar (Subject-Verb-Object), even if it sounds silly. |
| **Semantic** | **Meaning & Logic**. Does it actually make sense in reality? | *"Apple eats boy"* is syntactically OK, but **semantically meaningless** because apples can't eat humans! In code: `5 + "cat"` is grammatically valid, but semantically impossible! |
| **Operator** | The action symbol performing the task. | `+`, `-`, `*`, `/` |
| **Operands** | The values or variables being acted upon. | In `5 + 10`, `5` and `10` are operands. |
| **Type Coercion** | Secret automatic conversion done by the compiler behind your back. | If you write `float x = 5 + 2.5;`, compiler automatically converts `5` into `5.0`. |
| **Parse Tree** | A family tree showing grammar hierarchy. | Built by Syntax Analyzer. |

---

## 📌 Topic 1: What is Type Checking?

### 1. Definition
Type checking is the process within **Semantic Analysis** where the compiler verifies whether operators and their operands adhere to the language's typing rules.

### 2. Position in Compiler Pipeline
- **Input:** Parse Tree from Syntax Analyzer + Symbol Table
- **Component:** Type Checker (Semantic Analyzer)
- **Output:** Annotated Type-Checked Syntax Tree OR Semantic Error Report

### 3. Key Functions of a Type Checker
1. **Error Detection:** Catches invalid operations at compile time (e.g., `arr[3.14]` or adding a string to an integer).
2. **Type Coercion (Implicit Conversion):** Automatically inserts conversion nodes (e.g., widening `int` to `float` in `int + float`).
3. **Overload Resolution:** Picks the exact operator or function based on the parameter types (e.g., `+` for integers vs `+` for strings).

### 4. 5-Mark Exam Answer Template
- **Heading:** Definition of Type Checking
- **Diagram:** Block diagram with `[Parse Tree + Symbol Table] -> [Type Checker] -> [Annotated Tree / Errors]`
- **Functions:** Error detection, type coercion, operator overloading
- **Example:** Explain `float b = a + 2.5;` vs `int x = 5 + "apple";`
