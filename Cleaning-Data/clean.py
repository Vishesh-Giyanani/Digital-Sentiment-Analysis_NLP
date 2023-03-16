import pandas as pd

# read in the original csv file
df = pd.read_csv('hello.csv', encoding='latin1')

# drop rows with any null values
df.dropna(inplace=True)

# remove rows with any numeric values
df = df[~df.applymap(lambda x: isinstance(x, (int, float))).any(axis=1)]

# write cleaned data to a new csv file
df.to_csv('hello-copy.csv', index=False)
