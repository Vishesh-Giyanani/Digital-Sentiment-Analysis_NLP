import pandas as pd
import re
import numpy as np

#0, 1, 8, 80, 86, 140, 147, 218, 283, 310, 323, 25, 26, 27, 28, 29, 348, 349, 350, 351, 352, 353

df = pd.read_csv('./Native Data/Native.csv')

df2 = df
df2 = df.iloc[:, [0, 1, 8, 80, 86, 134, 141, 201, 212, 258, 265, 25, 26, 27, 28, 29, 284, 285, 286, 287, 288]].copy()

df3 = df2
df3 = df2.tail(-3)

df3.rename(columns={df3.columns[0]: "StartDate"}, inplace=True)
df3.rename(columns={df3.columns[1]: "EndDate"}, inplace=True)
df3.rename(columns={df3.columns[2]: "ResponseId"}, inplace=True)
df3.rename(columns={df3.columns[3]: "Appliances-Score"}, inplace=True)
df3.rename(columns={df3.columns[4]: "Appliances-Text"}, inplace=True)
df3.rename(columns={df3.columns[5]: "Locks-Score"}, inplace=True)
df3.rename(columns={df3.columns[6]: "Locks-Text"}, inplace=True)
df3.rename(columns={df3.columns[7]: "Interio-Score"}, inplace=True)
df3.rename(columns={df3.columns[8]: "Interio-Text"}, inplace=True)
df3.rename(columns={df3.columns[9]: "Security-Score"}, inplace=True)
df3.rename(columns={df3.columns[10]: "Security-Text"}, inplace=True)
df3.rename(columns={df3.columns[11]: "City"}, inplace=True)
df3.rename(columns={df3.columns[12]: "Age"}, inplace=True)
df3.rename(columns={df3.columns[13]: "Gender"}, inplace=True)
df3.rename(columns={df3.columns[14]: "Education"}, inplace=True)
df3.rename(columns={df3.columns[15]: "NCCS categorization"}, inplace=True)
df3.rename(columns={df3.columns[16]: "Occupation"}, inplace=True)
df3.rename(columns={df3.columns[17]: "Household Income"}, inplace=True)
df3.rename(columns={df3.columns[18]: "Marrital Status"}, inplace=True)
df3.rename(columns={df3.columns[19]: "Household Ages"}, inplace=True)
df3.rename(columns={df3.columns[20]: "Household Volunme"}, inplace=True)


print(df3)


#Find and Replace

pattern1 = r'Extremely\s+likely\s*10'
pattern2 = r'Not\s+at\s+all\s+likely\s*0'


lst = ["Appliances-Score", "Locks-Score", "Interio-Score", "Security-Score"]


for i in lst:
    df3[i] = df3[i].replace({pattern1: 10, pattern2: 0}, regex=True)
    




# Remove all non-ASCII characters

pattern3 = r'[^a-zA-Z0-9\s]+'

#lstE = ["Appliances-Text", "Locks-Text", "Interio-Text", "Security-Text"]

#for i in lstE:
#    df3[i] = df3[i].apply(lambda x: re.sub(pattern3, '', str(x)))

df3.to_csv('./NLP/Book2.csv')
