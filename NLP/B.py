import pandas as pd

# Read the csv file into a pandas DataFrame
df = pd.read_csv('./NLP/Final.csv') 

# Convert score and text columns to numeric data types
df['score'] = pd.to_numeric(df['score'], errors='coerce')
df['score1'] = pd.to_numeric(df['score'], errors='coerce')
df['score2'] = pd.to_numeric(df['score'], errors='coerce')
df['score3'] = pd.to_numeric(df['score'], errors='coerce')
df['text_Negative'] = pd.to_numeric(df['text_Negative'], errors='coerce')
df['text_Neutral'] = pd.to_numeric(df['text_Neutral'], errors='coerce')
df['text_Positive'] = pd.to_numeric(df['text_Positive'], errors='coerce')
df['text.1_Negative'] = pd.to_numeric(df['text.1_Negative'], errors='coerce')
df['text.1_Neutral'] = pd.to_numeric(df['text.1_Neutral'], errors='coerce')
df['text.1_Positive'] = pd.to_numeric(df['text.1_Positive'], errors='coerce')
df['text.2_Negative'] = pd.to_numeric(df['text.1_Negative'], errors='coerce')
df['text.2_Neutral'] = pd.to_numeric(df['text.1_Neutral'], errors='coerce')
df['text.2_Positive'] = pd.to_numeric(df['text.1_Positive'], errors='coerce')
df['text.3_Negative'] = pd.to_numeric(df['text.1_Negative'], errors='coerce')
df['text.3_Neutral'] = pd.to_numeric(df['text.1_Neutral'], errors='coerce')
df['text.3_Positive'] = pd.to_numeric(df['text.1_Positive'], errors='coerce')

# Define a function to calculate the label based on the given logic for Business Unit 1
def calculate_label(row):
    score = row['score']
    positive = row['text_Positive'] * 100
    negative = row['text_Negative'] * 100
    neutral = row['text_Neutral'] * 100

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
    score = row['score1']
    positive = row['text.1_Positive']  * 100
    negative = row['text.1_Negative']  * 100
    neutral = row['text.1_Neutral'] * 100

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
    score = row['score2']
    positive = row['text.2_Positive']  * 100
    negative = row['text.2_Negative'] * 100
    neutral = row['text.2_Neutral'] * 100

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
    score = row['score3']
    positive = row['text.3_Positive'] * 100
    negative = row['text.3_Negative'] * 100
    neutral = row['text.3_Neutral'] * 100

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
