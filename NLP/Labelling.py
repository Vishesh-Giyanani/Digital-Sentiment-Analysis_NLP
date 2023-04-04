##This code is written with respect to 'column names'

import pandas as pd

# Loading CSV file into a DataFrame
df = pd.read_csv('./NLP/Final.csv')

# Saving/overwriting the updated DataFrame to  CSV file
df.to_csv('./NLP/Final.csv', index=False)


# Convert score and text columns to numeric data types
df['Appliances-Score'] = pd.to_numeric(df['Appliances-Score'], errors='coerce')
df['Locks-Score'] = pd.to_numeric(df['Locks-Score'], errors='coerce')
df['Interio-Score'] = pd.to_numeric(df['Interio-Score'], errors='coerce')
df['Security-Score'] = pd.to_numeric(df['Security-Score'], errors='coerce')



# Define a function to calculate the label based on the given logic for Business Unit 1
def calculate_label(row):
    score = row['Appliances-Score']
    try:
        positive = float(row['Appliances-Score_Positive']) * 100
    except ValueError:
        positive = 0
   # positive = float(row['Appliances-Score_Positive']) * 100 if row['Appliances-Score_Positive'] != 'Null' else 0
    neutral = float(row['Appliances-Score_Neutral']) * 100 if row['Appliances-Score_Neutral'] != 'Null' else 0
    negative = float(row['Appliances-Score_Negative']) * 100 if row['Appliances-Score_Negative'] != 'Null' else 0
   

    if score >= 8 and positive >= 50:
        return 'Promoter'
    elif score < 8 and positive >= 50:
        return 'Revised Promoter'
    elif score <= 8 and (neutral + negative) >= 50:
        return 'Detractor'
    elif score >= 8 and (neutral + negative) >= 50:
        return 'Revised Detractor'
    else:
        return '  '

# Apply the calculate_label function to the DataFrame to create a new column called 'label'
df['label'] = df.apply(calculate_label, axis=1)

# Define another function to calculate the label for score1 for Business Unit 2
def calculate_label1(row):
    score = row['Locks-Score']
    try:
        positive = float(row['Locks-Score_Positive']) * 100
    except ValueError:
        positive = 0
    #positive = float(row['Locks-Score_Positive']) * 100 if row['Appliances-Score_Positive'] != 'Null' else 0
    neutral = float(row['Locks-Score_Neutral']) * 100 if row['Appliances-Score_Neutral'] != 'Null' else 0
    negative = float(row['Locks-Score_Negative']) * 100 if row['Appliances-Score_Negative'] != 'Null' else 0
   

    if score >= 8 and positive >= 50:
        return 'Promoter'
    elif score < 8 and positive >= 50:
        return 'Revised Promoter'
    elif score <= 8 and (neutral + negative) >= 50:
        return 'Detractor'
    elif score >= 8 and (neutral + negative) >= 50:
        return 'Revised Detractor'
    else:
        return '  '

# Apply the calculate_label1 function to the DataFrame to create a new column called 'label1'
df['label1'] = df.apply(calculate_label1, axis=1)

# Define another function to calculate the label for score2 for Business Unit 3
def calculate_label2(row):
    score = row['Interio-Score']
    try:
        positive = float(row['Interio-Score_Positive']) * 100
    except ValueError:
        positive = 0
    #positive = float(row['Interio-Score_Positive']) * 100 if row['Appliances-Score_Positive'] != 'Null' else 0
    neutral = float(row['Interio-Score_Neutral']) * 100 if row['Appliances-Score_Neutral'] != 'Null' else 0
    negative = float(row['Interio-Score_Negative']) * 100 if row['Appliances-Score_Negative'] != 'Null' else 0
   

    if score >= 8 and positive >= 50:
        return 'Promoter'
    elif score < 8 and positive >= 50:
        return 'Revised Promoter'
    elif score <= 8 and (neutral + negative) >= 50:
        return 'Detractor'
    elif score >= 8 and (neutral + negative) >= 50:
        return 'Revised Detractor'
    else:
        return '  '
 
# Apply the calculate_label2 function to the DataFrame to create a new column called 'label2'
df['label2'] = df.apply(calculate_label2, axis=1)

# Define another function to calculate the label for score3 for Business Unit 4
def calculate_label3(row):
    score = row['Security-Score']
    try:
        positive = float(row['Security-Score_Positive']) * 100
    except ValueError:
        positive = 0
    #positive = float(row['Security-Score_Positive']) * 100 if row['Appliances-Score_Positive'] != 'Null' else 0
    neutral = float(row['Security-Score_Neutral']) * 100 if row['Appliances-Score_Neutral'] != 'Null' else 0
    negative = float(row['Security-Score_Negative']) * 100 if row['Appliances-Score_Negative'] != 'Null' else 0

    if score >= 8 and positive >= 50:
        return 'Promoter'
    elif score < 8 and positive >= 50:
        return 'Revised Promoter'
    elif score <= 8 and (neutral + negative) >= 50:
        return 'Detractor'
    elif score >= 8 and (neutral + negative) >= 50:
        return 'Revised Detractor'
    else:
        return '  '

# Apply the calculate_label3 function to the DataFrame to create a new column called 'label3'
df['label3'] = df.apply(calculate_label3, axis=1)

# Write the updated DataFrame to a new csv file
df.to_csv('./NLP/Final2.csv', index=False)


