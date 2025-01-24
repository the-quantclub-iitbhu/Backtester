def perform_backtest_compound(csv_file_path: str, leverage: float = 1.0) -> None:
    """
    Perform a compound backtest of a trading strategy using the provided CSV file.

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
        Outputs a CSV file containing returns, cumulative returns, and account balance.

    Notes:
    ------
    - This method assumes an initial account balance of 1000 units.
    - Transaction costs are proportional to the account balance (0.0015%).

    Example:
    -------
    >>> perform_backtest_compound('sample_trading_data.csv')
    """
    df = pd.read_csv(csv_file_path)
    amount_in_account = 1000
    pnl = 0
    trades_entered = 0
    trades_exited = 0
    df['returns'] = 0
    df['cumulative_return'] = 0
    df['amount_in_account'] = 0

    for i in range(len(df)):
        current_pos = df.loc[i, 'net_position']
        if current_pos in [1, -1]:
            trades_entered += 1
            entry_price = df.loc[i, 'close']
            for j in range(i + 1, len(df)):
                next_pos = df.loc[j, 'net_position']
                if next_pos == 0 or abs(next_pos - current_pos) == 2:
                    exit_price = df.loc[j, 'close']
                    pnl += ((exit_price - entry_price) / entry_price * amount_in_account * current_pos - 0.0015 * amount_in_account) * leverage
                    df.loc[j, 'cumulative_return'] = pnl
                    df.loc[j, 'returns'] = ((exit_price - entry_price) / entry_price * amount_in_account * current_pos - 0.0015 * amount_in_account) * leverage
                    trades_exited += 1
                    amount_in_account += df.loc[j, 'returns']
                    df.loc[j, 'amount_in_account'] = amount_in_account
                    i = j + 1
                    break
    print(f"PnL with time: {pnl}")
    print(f"Trades Entered: {trades_entered}")
    print(f"Trades Exited: {trades_exited}")
    df.to_csv(f'final_file_compound_{csv_file_path}.csv')
