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
    
    positive = float(row['Appliances-Text_Positive']) * 100 if row['Appliances-Text_Positive'] != 'Null' else 0
    neutral = float(row['Appliances-Text_Neutral']) * 100 if row['Appliances-Text_Neutral'] != 'Null' else 0
    negative = float(row['Appliances-Text_Negative']) * 100 if row['Appliances-Text_Negative'] != 'Null' else 0
   

      #previous logic
    #(if score >= 8 and positive >= 50: return 'Promoter'
    #elif score < 8 and positive >= 50: return 'Revised Promoter'
    #elif score <= 8 and (neutral + negative) >= 50: return 'Detractor'
    #elif score >= 8 and (neutral + negative) >= 50: return 'Revised Detractor'
    #else: return None''
    
    # new logic for labelling
    if  positive >= 70 :
        return 'Promoter'
    elif negative >= 60 :
        return 'Detractor'
    elif positive == 0 :
        return None
    else:
        return 'passive'

# Apply the calculate_label function to the DataFrame to create a new column called 'Appliances_label'
df['Appliances_label'] = df.apply(calculate_label, axis=1)

# Define another function to calculate the label for score1 for Business Unit 2
def calculate_label1(row):
    
    score = row['Locks-Score']
    
    positive = float(row['Locks-Text_Positive']) * 100 if row['Locks-Text_Positive'] != 'Null' else 0
    neutral = float(row['Locks-Text_Neutral']) * 100 if row['Locks-Text_Neutral'] != 'Null' else 0
    negative = float(row['Locks-Text_Negative']) * 100 if row['Locks-Text_Negative'] != 'Null' else 0
   

      #previous logic
    #(if score >= 8 and positive >= 50: return 'Promoter'
    #elif score < 8 and positive >= 50: return 'Revised Promoter'
    #elif score <= 8 and (neutral + negative) >= 50: return 'Detractor'
    #elif score >= 8 and (neutral + negative) >= 50: return 'Revised Detractor'
    #else: return None''
    
    # new logic for labelling
    if  positive >= 70 :
        return 'Promoter'
    elif negative >= 60 :
        return 'Detractor'
    elif negative == 0 :
        return None
    else:
        return 'passive'

# Apply the calculate_label1 function to the DataFrame to create a new column called 'Locks_label'
df['Locks_label'] = df.apply(calculate_label1, axis=1)

# Define another function to calculate the label for score2 for Business Unit 3
def calculate_label2(row):
    
    score = row['Interio-Score']
    
    positive = float(row['Interio-Text_Positive']) * 100 if row['Interio-Text_Positive'] != 'Null' else 0
    neutral = float(row['Interio-Text_Neutral']) * 100 if row['Interio-Text_Neutral'] != 'Null' else 0
    negative = float(row['Interio-Text_Negative']) * 100 if row['Interio-Text_Negative'] != 'Null' else 0
   
   
      #previous logic
    #(if score >= 8 and positive >= 50: return 'Promoter'
    #elif score < 8 and positive >= 50: return 'Revised Promoter'
    #elif score <= 8 and (neutral + negative) >= 50: return 'Detractor'
    #elif score >= 8 and (neutral + negative) >= 50: return 'Revised Detractor'
    #else: return None''
    
    # new logic for labelling
    if  positive >= 70 :
        return 'Promoter'
    elif negative >= 60 :
        return 'Detractor'
    elif negative == 0 :
        return None
    else:
        return 'passive'
# Apply the calculate_label2 function to the DataFrame to create a new column called 'Interio_label'
df['Interio_label'] = df.apply(calculate_label2, axis=1)

# Define another function to calculate the label for score3 for Business Unit 4
def calculate_label3(row):
    
    score = row['Security-Score']
   
    positive = float(row['Security-Text_Positive']) * 100 if row['Security-Text_Positive'] != 'Null' else 0
    neutral = float(row['Security-Text_Neutral']) * 100 if row['Security-Text_Neutral'] != 'Null' else 0
    negative = float(row['Security-Text_Negative']) * 100 if row['Security-Text_Negative'] != 'Null' else 0
   
   
    #previous logic
    #(if score >= 8 and positive >= 50: return 'Promoter'
    #elif score < 8 and positive >= 50: return 'Revised Promoter'
    #elif score <= 8 and (neutral + negative) >= 50: return 'Detractor'
    #elif score >= 8 and (neutral + negative) >= 50: return 'Revised Detractor'
    #else: return None''
    
    # new logic for labelling
    if  positive >= 70 :
        return 'Promoter'
    elif negative >= 60 :
        return 'Detractor'
    elif negative == 0 :
        return None
    else:
        return 'passive'

# Apply the calculate_label3 function to the DataFrame to create a new column called 'Security_label'
df['Security_label'] = df.apply(calculate_label3, axis=1)

# Write the updated DataFrame to a new csv file
df.to_csv('./NLP/Final2.csv', index=False)


