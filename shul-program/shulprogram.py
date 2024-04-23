import pandas as pd
import os

directory_path = '/Users/connor/Documents/OneDrive/Collated Programs/Shul Program/'

# Get a list of CSV files in the specified directory
csv_files = [file for file in os.listdir(directory_path) if file.endswith('.csv')]

# Create an empty dictionary to store the data and totals
data_dict = {}

# Iterate through each CSV file, read its data, calculate totals, and store it in the dictionary
for file in csv_files:
    file_path = os.path.join(directory_path, file)
    
    # Read CSV file
    df = pd.read_csv(file_path)
    
    # Check if the DataFrame is not empty before processing
    if not df.empty:
        # Calculate totals for each event
        totals_df = df.groupby('Event').sum().reset_index()
        
        # Use the file name as the key (without the extension)
        key = os.path.splitext(file)[0]
        
        # Store both the original DataFrame and the totals DataFrame in the dictionary
        data_dict[key] = {'data': df, 'totals': totals_df}

# Display or further process the data and totals stored in the dictionary
for key, data in data_dict.items():
    print(f"Data from {key}:")
    print(data['data'])
    
    print(f"\nTotals for {key}:")
    print(data['totals'])
    print("\n")

