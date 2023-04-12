import pandas as pd

# Define the columns to extract
columns_to_extract = ['Appliances_label', 'Locks_label', 'Security_label','Interio_label']

# Load the original CSV file into a pandas DataFrame
df = pd.read_csv('Final2.csv')

# Create a new DataFrame containing only the selected columns
new_df = df[columns_to_extract]

# Save the new DataFrame to a new CSV file
new_df.to_csv('new_file.csv', index=False)