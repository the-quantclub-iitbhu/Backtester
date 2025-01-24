# Backtesting Strategies

### Overview
This repository provides two powerful backtesting methods for evaluating algorithmic trading strategies:
1. **Static Backtesting**: Tracks performance with a fixed capital base.
2. **Compound Backtesting**: Adjusts the trading capital dynamically based on account growth.

These tools allow traders and quants to assess the profitability and performance of trading strategies using historical data. The backtester handles trade entries, exits, and calculates key performance metrics like cumulative returns, profit and loss (PnL), and trade counts.

---

### Features
- **Static Backtesting**: 
   - Calculates profits and losses using a constant capital base.
   - Tracks cumulative returns for a clear view of strategy performance.
- **Compound Backtesting**: 
   - Adjusts capital dynamically based on account balance.
   - Incorporates leverage and trading costs for realistic simulations.
- **Customizable Parameters**:
   - Leverage levels.
   - Trading costs.
- Outputs results in a CSV file for further analysis.

---

### Requirements
To use the backtester, ensure you have the following dependencies installed:

- Python 3.7+
- `pandas`
- `numpy`

You can install the required packages using:
```bash
pip install pandas numpy
```

---

### Usage
Clone the repository to your local machine:
```bash
git clone https://github.com/your-username/backtesting-strategies.git
cd backtesting-strategies
```

#### Functions
1. **`perform_backtest_static`**
   - Runs a static backtest using the provided CSV file.
   - Example:
     ```python
     perform_backtest_static('your_data.csv', leverage=2)
     ```
   - Output: Creates a file named `final_file_your_data.csv` with results.

2. **`perform_backtest_compound`**
   - Runs a compound backtest using the provided CSV file.
   - Example:
     ```python
     perform_backtest_compound('your_data.csv', leverage=2)
     ```
   - Output: Creates a file named `final_file_compound_your_data.csv` with results.

---

### CSV File Format
The input CSV file should have the following columns:
- `datetime`: The timestamp of the data (e.g., `YYYY-MM-DD HH:MM:SS`).
- `close`: Closing price of the asset.
- `net_position`: Net position for the trade (`1` for long, `-1` for short, `0` for no position).
- `volume`: (Optional) Volume data for calculations.

Example:
| datetime            | close   | net_position | volume  |
|---------------------|---------|--------------|---------|
| 2023-01-01 10:00:00 | 100.50  | 1            | 2000    |
| 2023-01-01 10:05:00 | 101.00  | 0            | 1500    |
| 2023-01-01 10:10:00 | 99.75   | -1           | 2500    |

---

### Example Walkthrough
#### Running a Static Backtest
```python
from backtester import perform_backtest_static

# Run the static backtest
perform_backtest_static('data.csv', leverage=1.5)
```
#### Running a Compound Backtest
```python
from backtester import perform_backtest_compound

# Run the compound backtest
perform_backtest_compound('data.csv', leverage=1.5)
```

---

### Outputs
Both functions produce a CSV file with the following columns:
- `datetime`: Timestamp of the event.
- `returns`: Per-trade returns.
- `cumulative_return`: Cumulative PnL over the test period.
- (For compound backtest) `amount_in_account`: Tracks the account balance over time.

---

### Contribution
Contributions are welcome! If you'd like to add features, optimize performance, or fix bugs:
1. Fork the repository.
2. Create a new branch (`feature/my-feature`).
3. Submit a pull request.

---

### License
This project is licensed under the MIT License. See the `LICENSE` file for details.

---

Happy backtesting! 🚀

