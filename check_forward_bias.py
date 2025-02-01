import pandas as pd

# Load results and historical data
result_file = pd.read_csv("results.csv")
result_file = result_file[result_file['signals'] != 0]  # Filter non-zero signals

data_8h = pd.read_csv("BTC_2019_2023_8h.csv", index_col="Unnamed: 0")

# Convert datetime columns to pandas datetime format
result_file['datetime'] = pd.to_datetime(result_file['datetime'])
data_8h['datetime'] = pd.to_datetime(data_8h['datetime'])

i = 0  # Counter to track lookahead bias

# Loop through signals in reverse order
for row in result_file.iloc[::-1].itertuples():
    ind = data_8h[data_8h['datetime'] == row.datetime].index

    if len(ind) == 0:
        continue  # Skip if datetime not found

    data = data_8h[:ind[0] + 1]  # Use only data up to this point

    # Process the data (assumed functions)
    processed_data = process_data(data)  
    result_data = strat(processed_data)

    # Get last signal
    signal = result_data['signals'].iloc[-1]

    # Check if signal changes due to future data leakage
    if signal == row.signals:
        continue
    else:
        print("Lookahead bias found!")
        i += 1
        break  # Stop checking after first detection

# Final validation
if i == 0:
    print("No lookahead bias detected!")
