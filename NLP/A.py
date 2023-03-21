from transformers import AutoTokenizer, AutoModelForSequenceClassification
from scipy.special import softmax
import pandas as pd

# Load the model and tokenizer
roberta = "cardiffnlp/twitter-roberta-base-sentiment"
model = AutoModelForSequenceClassification.from_pretrained(roberta)
tokenizer = AutoTokenizer.from_pretrained(roberta)

labels = ['Negative', 'Neutral', 'Positive']

# Read the CSV file
df = pd.read_csv('NLP/Book2.csv')

# Select the columns to analyze
columns_to_analyze = [5, 7, 9, 11]
text_columns = df.columns[columns_to_analyze]

# Iterate over the text columns of the DataFrame
for text_column in text_columns:
    # Get the index of the current text column
    text_column_index = df.columns.get_loc(text_column)

    # Iterate over the rows of the DataFrame
    for index, row in df.iterrows():
        tweet = str(row[text_column_index])

        # Preprocess the tweet
        tweet_words = []
        for word in tweet.split(' '):
            if word.startswith('@') and len(word) > 1:
                word = '@user'
            elif word.startswith('http'):
                word = 'http'
            tweet_words.append(word)
        tweet_processed = ' '.join(tweet_words)

        # Sentiment analysis
        encoded_tweet = tokenizer(tweet_processed, return_tensors='pt')
        output = model(**encoded_tweet)
        scores = output[0][0].detach().numpy()
        scores = softmax(scores)

        # Update the DataFrame with the sentiment scores
        for i in range(len(scores)):
            l = labels[i]
            s = scores[i]
            df.at[index, f"{text_column}_{l}"] = s

# Save the updated DataFrame to the CSV file
df.to_csv('NLP/Final.csv', index=False)