import pandas as pd

# Load the original CSV file into a pandas DataFrame
df = pd.read_csv('./NLP/Final2.csv')


# Define the columns to extract
columns_Appliances = ['StartDate', 'EndDate', 'ResponseId', 'Appliances-Score', 'Appliances-Text', 'Appliances-Text_Negative', 'Appliances-Text_Neutral', 'Appliances-Text_Positive', 'Appliances_label',
                        'City', 'Age','Gender','Education','NCCS categorization', 'Occupation','Household Income','Marrital Status','Household Ages','Household Volume']
columns_Locks = ['StartDate', 'EndDate', 'ResponseId', 'Appliances-Score','Locks-Score', 'Locks-Text', 'Locks-Text_Negative', 'Locks-Text_Neutral', 'Locks-Text_Positive', 'Locks_label',
                     'City', 'Age','Gender','Education','NCCS categorization', 'Occupation','Household Income','Marrital Status','Household Ages','Household Volume']
columns_Interio = ['StartDate', 'EndDate', 'ResponseId', 'Appliances-Score','Interio-Score', 'Interio-Text', 'Interio-Text_Negative', 'Interio-Text_Neutral', 'Interio-Text_Positive', 'Interio_label',
                        'City', 'Age','Gender','Education','NCCS categorization', 'Occupation','Household Income','Marrital Status','Household Ages','Household Volume']
columns_Security = ['StartDate', 'EndDate', 'ResponseId', 'Appliances-Score','Security-Score', 'Security-Text', 'Security-Text_Negative','Security-Text_Neutral','Security-Text_Positive','Security-Score','Security_label',
                        'City', 'Age','Gender','Education','NCCS categorization', 'Occupation','Household Income','Marrital Status','Household Ages','Household Volume']



# Create a new DataFrame containing only the selected columns
ca_df = df[columns_Appliances]
cl_df = df[columns_Locks]
ci_df = df[columns_Interio]
cs_df = df[columns_Security]

# Save the new DataFrame to a new CSV file
ca_df.to_csv('./NLP/Appliances.csv', index=False)
cl_df.to_csv('./NLP/Locks.csv', index=False)
ci_df.to_csv('./NLP/Interio.csv', index=False)
cs_df.to_csv('./NLP/Security.csv', index=False)
