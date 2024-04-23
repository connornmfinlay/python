import pandas as pd
import os

# Specify the directory containing your CSV files
directory_path = '/Users/connor/Documents/OneDrive/Collated Programs/Shul Program/'

# Get a list of CSV files in the specified directory
csv_files = [file for file in os.listdir(directory_path) if file.endswith('.csv')]

# Create an empty list to store DataFrames
data_frames = []

# Iterate through each CSV file, read its data, and store it in the list
for file in csv_files:
    file_path = os.path.join(directory_path, file)
    
    # Read CSV file
    df = pd.read_csv(file_path)
    
    # Check if the DataFrame is not empty before processing
    if not df.empty:
        # Store the DataFrame in the list
        data_frames.append(df)

# Combine the DataFrames in the list into a single DataFrame
combined_df = pd.concat(data_frames, keys=[f"Data_{i}" for i in range(len(data_frames))])

# Calculate totals for each event in the combined DataFrame
annual_totals_df = combined_df.groupby('Event').sum().reset_index()

# Write the combined DataFrame to a new CSV file
output_file_path = os.path.join(directory_path, 'annual_total.csv')
annual_totals_df.to_csv(output_file_path, index=False)

print(f"Combined totals written to {output_file_path}")
