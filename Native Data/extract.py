import pandas as pd

#0, 1, 8, 80, 86, 140, 147, 218, 283, 310, 323, 25, 26, 27, 28, 29, 348, 349, 350, 351, 352, 353

df = pd.read_csv('./Native Data/Native.csv')    

df2 = df.iloc[: , [0, 1, 8, 80, 86, 140, 147, 218, 283, 310, 323, 25, 26, 27, 28, 29, 348, 349, 350, 351, 352, 353]].copy()

df2.to_csv('./Cleaning-Data\Fresh.csv')