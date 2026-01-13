# ComputorV1

A program that parses and solves polynomial equations (degree 0, 1, or 2) written in a strict format.

## Requirements

- Python 3.10+ (recommended)

## Install / Setup

Clone the repo and run from the project root:

```bash
python3 --version
```

## Usage

Run the program with a single argument: the equation in quotes.

```bash
python3 computor.py "2 * X^2 - 1 * X^0 = 3 * X^2"
```

If the argument is missing:

```bash
python3 computor.py
# Usage: python3 computor.py "<equation>"
```

## Input format

Your equation must respect the following rules:

- Variable must be **`X`** (uppercase only)
- Each term must be written like: **`<coef> * X^<exp>`**
- `coef` can be integer or float (examples: `2`, `-3`, `0.5`)
- `exp` must be a non-negative integer (examples: `0`, `1`, `2`)
- Use spaces around `=`, `*`, `+`, `-` exactly as in examples

Examples of valid terms:
- `5 * X^0`
- `-3 * X^1`
- `0.5 * X^2`

## Output

The program prints:

- The reduced form: `... = 0`
- The polynomial degree
- The solution(s), depending on the degree and discriminant

## Examples

### Degree 0
```bash
python3 computor.py "5 * X^0 = 0 * X^0"
Reduced form: 5 * X^0 = 0
Polynomial degree: 0
No solution
```

```bash
python3 computor.py "0 * X^0 = 0 * X^0"
Reduced form: 0 = 0
Polynomial degree: 0
All real numbers are solutions
```

### Degree 1
```bash
python3 computor.py "2 * X^1 + 4 * X^0 = 0 * X^0"

Reduced form: 4 * X^0 + 2 * X^1 = 0
Polynomial degree: 1

        Steps:
        a = 2
        b = 4

        x = -b / a
        x = -4 / 2
        x = -2

The solution is:
-2
```

### Degree 2 (complex solutions example)
```bash
python3 computor.py "3 * X^2 + 6 * X^1 + 13 * X^0 = 0 * X^0"
Reduced form: 13 * X^0 + 6 * X^1 + 3 * X^2 = 0
Polynomial degree: 2

        Steps:
        a = 3
        b = 6
        c = 13

        Δ = b² - 4ac
        Δ = 36 - (156)
        Δ = -120

        Δ < 0 → two complex solutions

        x1 = (-b - i√|Δ|) / (2a)
        x2 = (-b + i√|Δ|) / (2a)

        x1 = -1 + 1.825742*i
        x2 = -1 - 1.825742*i

Discriminant is strictly negative, the complex solutions are:
-1 + 1.825742*i
-1 - 1.825742*i
```

## Limits

- Supported degrees: **0, 1, 2**
- If degree > 2, the program prints an error message and stops.

## Tests / Sample cases

Sample equations and expected outputs are available in:

- `tests/examples.md`

## 42 Project

This project was made as part of the **42** curriculum.