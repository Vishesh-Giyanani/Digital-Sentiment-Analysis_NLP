import pandas as pd
import numpy as np

df = pd.read_csv('./NLP/Book2.csv')

df2 = df.iloc[: , [5,7,9,11]].copy()


df2 = df2.where(~df2.apply(lambda row: row.str.isalpha()).all(axis=1), other=np.nan)

df2.to_csv('./NLP/trial.csv', index=False)
