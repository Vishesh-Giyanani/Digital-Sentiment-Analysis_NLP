import pandas as pd

#0, 1, 8, 80, 86, 140, 147, 218, 283, 310, 323, 25, 26, 27, 28, 29, 348, 349, 350, 351, 352, 353

df = pd.read_csv('./Native Data/Native.csv')    

df2=df
df2 = df.iloc[: , [0, 1, 8, 80, 86, 134, 141, 201, 212, 258, 265, 25, 26, 27, 28, 29, 284, 285, 286, 287, 288, 284]].copy()

df3= df2.tail(-3)

df3.rename(columns={ df3.columns[0]: "StartDate" }, inplace = True)
df3.rename(columns={ df3.columns[1]: "EndDate" }, inplace = True)
df3.rename(columns={ df3.columns[2]: "ResponseId" }, inplace = True)
df3.rename(columns={ df3.columns[3]: "StartDate" }, inplace = True)
df3.rename(columns={ df3.columns[1]: "EndDate" }, inplace = True)
df3.rename(columns={ df3.columns[1]: "EndDate" }, inplace = True)
df3.rename(columns={ df3.columns[0]: "StartDate" }, inplace = True)
df3.rename(columns={ df3.columns[1]: "EndDate" }, inplace = True)
df3.rename(columns={ df3.columns[1]: "EndDate" }, inplace = True)
df3.rename(columns={ df3.columns[0]: "StartDate" }, inplace = True)
df3.rename(columns={ df3.columns[1]: "EndDate" }, inplace = True)
df3.rename(columns={ df3.columns[1]: "EndDate" }, inplace = True)
df3.rename(columns={ df3.columns[0]: "StartDate" }, inplace = True)
df3.rename(columns={ df3.columns[1]: "EndDate" }, inplace = True)
df3.rename(columns={ df3.columns[1]: "EndDate" }, inplace = True)
df3.rename(columns={ df3.columns[0]: "StartDate" }, inplace = True)
df3.rename(columns={ df3.columns[1]: "EndDate" }, inplace = True)
df3.rename(columns={ df3.columns[1]: "EndDate" }, inplace = True)
df3.rename(columns={ df3.columns[0]: "StartDate" }, inplace = True)
df3.rename(columns={ df3.columns[1]: "EndDate" }, inplace = True)
df3.rename(columns={ df3.columns[1]: "EndDate" }, inplace = True)
df3.rename(columns={ df3.columns[1]: "EndDate" }, inplace = True)








print(df3)

df3.to_csv('./NLP/Book2.csv')