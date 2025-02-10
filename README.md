# Simple Expression Calculator

A custom Python calculator that evaluates arithmetic expressions with support for nested parentheses, negative numbers, and implicit multiplication. The calculator also approximates the result as both a decimal and a fraction.

## Overview

This project implements an arithmetic expression evaluator using a **divide-and-conquer** strategy. Instead of trying to parse and evaluate the entire expression at once, the algorithm repeatedly finds and simplifies the smallest evaluable sub-expression—such as the innermost parentheses—and reduces the overall expression step by step.

**Key Point:**  
This code is written entirely from scratch without relying on any Python-specific modules or advanced features. Everything—from tokenization to evaluation and fraction approximation—is implemented using basic Python constructs. This approach is especially beneficial for learning, as it forces you to think through each step of the algorithm and understand the underlying logic.

## Features

- **Nested Parentheses:**  
  Handles expressions with multiple levels of nested brackets.
  
- **Implicit Multiplication:**  
  Automatically assumes multiplication when a number or closing bracket is directly followed by an opening bracket (e.g., `2(3+4)` becomes `2*(3+4)`).

- **Negative Numbers:**  
  Correctly processes negative numbers by treating the minus sign as part of the number when appropriate.

- **Operator Precedence:**  
  Processes multiplication and division before addition and subtraction.

- **Decimal-to-Fraction Approximation:**  
  After computation, the calculator approximates the result to a fraction using a tolerance-based approach.

- **Pure Python Implementation:**  
  The entire algorithm is built using core Python language features only. No specialized modules or libraries are used, which helps in understanding the fundamentals of how expressions can be parsed and evaluated.

## How It Works

1. **Tokenization:**  
   The input string is parsed into a list of tokens (numbers and operators). Special care is taken to:
   - Include negative numbers (by checking if a `-` appears at the start or immediately after an opening parenthesis).
   - Separate multi-digit numbers and decimals properly.
   
2. **Implicit Multiplication Handling:**  
   The algorithm scans the token list to automatically insert multiplication operators in cases where an implicit multiplication is expected (e.g., before a `(` or after a `)`).

3. **Evaluation of Expressions:**  
   - **Innermost Parentheses:**  
     The algorithm locates the innermost pair of parentheses and evaluates the expression inside.
   - **Operator Processing:**  
     Within each sub-expression, multiplication and division are processed before addition and subtraction.
   - **Iterative Reduction:**  
     By repeatedly evaluating small sub-expressions, even complex expressions are reduced step by step until a single final result is obtained.

4. **Decimal to Fraction Conversion:**  
   Once the final result is computed (as a float), it is converted into a fraction. The conversion works by incrementally finding a denominator that approximates the decimal within a small tolerance.

## Usage

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/devharshmehta/simple-expression-calculator.git
   cd simple-expression-calculator

2. **Run the Calculator:** 
    
    Ensure you have Python installed, then run:
    
    ```bash
    python calc.py

3. **Enter an Expression:**

    When prompted, type in your arithmetic expression. For example:

    ```bash
    enter: 2(3+4)-5/2
    ```

    **Note:**

    - Do not add spaces in the input.
    - Avoid duplicating operators.
    - Ensure that all brackets are properly closed.
    - The program will output the result both as a decimal and as an approximated fraction.

## Example

For the input:
```bash
2(3+4)-5/2
```
The calculator processes the expression as follows:

- **Tokenization:** Converts input to tokens, handling the implicit multiplication `(2*(3+4))`.
- **Evaluation:**
    - Resolves `(3+4)` to `7`.
    - Computes `2*7` to get `14`.
    - Then computes `14-5/2` resulting in `11.5`.
- **Fraction Approximation:** Converts `11.5` to a fraction (e.g., `23/2`).
The output will be:
```bash
11.5 or 23/2
```
## Disclaimer
This project is intended solely for learning the basics of programming and understanding how to translate your thoughts into computer code. **Important Limitations:**

- **Input Validation:**
    Input validation is minimal. Please do not add spaces, avoid duplicating operators, and ensure that all brackets are properly closed.
- **Learning Focus:**
    The focus is on grasping fundamental programming concepts rather than building a production-ready calculator.
