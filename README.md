A Python CLI tool that calculates financial outcomes for investments and home loans. Users choose between calculating simple or compound interest on investments, or computing monthly mortgage repayment amounts on bonds. It's a learning project or utility for quick financial calculations.

### Stack
- **Language:** Python (100%)
- **Runtime:** Standard Python interpreter (no framework)
- **Libraries:** `math` module (for `pow()` function)

## How it's organized

```
finance_calculators.py    Main CLI script with menu-driven interface
LICENSE                   Apache 2.0 license
```

**How it fits together:** The script runs as a single executable file. It presents a menu prompt, accepts user input to select either investment or bond calculation, gathers financial parameters through sequential prompts, applies the appropriate formula, and prints the result.

## How to run it

```bash
python finance_calculators.py
```

Follow the on-screen prompts to choose between investment or bond calculation, then enter the required values (principal, interest rate, time period, etc.).

### Compound Interest Formula

On **line 34**, the compound interest calculation is:

```python
p * math.pow((1 + (r/100)),t)
```

Where:
- **p** = principal (initial investment amount)
- **r** = annual interest rate (as a percentage, e.g., 8 for 8%)
- **t** = time period in years

This implements the standard compound interest formula: **A = P(1 + r)^t**, where the interest is compounded annually. The result represents the total amount you'll have after the investment period.

---

### Bond Repayment Calculation

On **line 41**, the monthly bond repayment is calculated as:

```python
(i/100) * p / (1 - (1 + (i/100))*(-n))
```

Where:
- **p** = present value of the house (loan principal)
- **i** = annual interest rate (as a percentage)
- **n** = number of months to repay

This implements the **standard amortization formula** for monthly mortgage payments. Breaking it down:
- `(i/100) * p` = the numerator (monthly interest rate × principal)
- `1 - (1 + (i/100))*(-n)` = the denominator (discount factor based on the repayment period)

The formula calculates a fixed monthly payment amount that covers both principal and interest over the loan term. Note: there's a **bug in line 41** — the interest rate should be divided by 12 for a monthly rate, but the code uses the annual rate directly, which will produce incorrect results.
