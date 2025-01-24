import pandas as pd

def perform_backtest_static(csv_file_path: str, leverage: float = 1.0) -> None:
    """
    Perform a static backtest of a trading strategy using the provided CSV file.

    Parameters:
    ----------
    csv_file_path : str
        Path to the CSV file containing trading data. The file must include 'net_position' 
        and 'close' columns.
    leverage : float, optional
        Leverage to apply during the backtest, default is 1.0.

    Returns:
    -------
    None
        Outputs a CSV file containing returns and cumulative returns.

    Notes:
    ------
    - This method assumes a fixed initial capital of 1000 units.
    - Transaction costs are fixed at 1.5 units per trade.

    Example:
    -------
    >>> perform_backtest_static('sample_trading_data.csv')
    """
    df = pd.read_csv(csv_file_path)
    initial_amount = 1000
    pnl = 0
    trades_entered = 0
    trades_exited = 0
    df['returns'] = 0
    df['cumulative_return'] = 0
    
    for i in range(len(df)):
        current_pos = df.loc[i, 'net_position']
        if current_pos in [1, -1]:
            trades_entered += 1
            entry_price = df.loc[i, 'close']
            for j in range(i + 1, len(df)):
                next_pos = df.loc[j, 'net_position']
                if next_pos == 0 or abs(next_pos - current_pos) == 2:
                    exit_price = df.loc[j, 'close']
                    pnl += ((exit_price - entry_price) / entry_price * initial_amount * current_pos - 1.5) * leverage
                    df.loc[j, 'cumulative_return'] = pnl
                    df.loc[j, 'returns'] = ((exit_price - entry_price) / entry_price * initial_amount * current_pos - 1.5) * leverage
                    trades_exited += 1
                    break
            i = j + 1
    print(f"Final PnL: {pnl}")
    print(f"Trades Entered: {trades_entered}")
    print(f"Trades Exited: {trades_exited}")
    df.to_csv(f'final_file_{csv_file_path}.csv')
