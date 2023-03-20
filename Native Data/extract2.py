import pandas as pd
import numpy as np
from spellchecker import SpellChecker

df = pd.read_csv('./NLP/Book2.csv')

df2 = df.iloc[: , [5,7,9,11]].copy()


df2 = df2.where(~df2.apply(lambda row: row.str.isalpha()).all(axis=1), other=np.nan)

for index, row in df.iterrows():
    text = str(row)

    # Initialize spell checker
    spell = SpellChecker()

    # Split the text into words
    words = text.split()

    # Check for spelling errors
    misspelled_words = spell.unknown(words)

    corrected_word = ''

    # Correct spelling errors
    for word in misspelled_words:
        corrected_word = str(spell.correction(word))
        text = text.replace(word, corrected_word)

    df2.to_csv('NLP/Final2.csv', index=False)