import pandas as pd

#0, 1, 8, 80, 86, 140, 147, 218, 283, 310, 323, 25, 26, 27, 28, 29, 348, 349, 350, 351, 352, 353

df = pd.read_csv('./Native Data/Native.csv')    

df2 = df.iloc[: , [0, 1, 8, 80, 86, 134, 141, 201, 212, 258, 265, 25, 26, 27, 28, 29, 284, 285, 286, 287, 288, 284]].copy()

print(df2)

df2.to_csv('./NLP/Book2.csv')