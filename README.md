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

