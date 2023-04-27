import pandas as pd
import matplotlib.pyplot as plt

# read the CSV file into a DataFrame
df = pd.read_csv("./NLP/Final.csv")
 
# define the columns to search
columns_to_search = ["Appliances-Text"]

# define the lists of keywords for each category
product_keywords = ['design', 'modern', 'stylish', 'attractive', 'features', 'quality', 'durable', 'long lasting', 'material', 'innovation']
price_keywords = ['costly', 'high price', 'market pricing']
range_keywords = ['wide options']
availability_keywords = ['limited', 'online', 'offline', 'stores']
servicing_keywords = ['servicing', 'customer service']
reviews_keywords = ['reviews', 'bad remarks']
brand_keywords = ['brand', 'brand image', 'trust', 'legacy', 'heritage', 'reliable']
experience_keywords = ['experience', 'reviews', 'ratings', 'friends', 'family']

# initialize a dictionary to store the total scores for each category
total_scores = {'product': 0, 'price': 0, 'range': 0, 'availability': 0, 'servicing': 0, 'reviews': 0, 'brand': 0, 'experience': 0}

# loop through each row in the DataFrame
for i, row in df.iterrows():
    # initialize a dictionary to store the scores for each category for the current row
    scores = {'product': 0, 'price': 0, 'range': 0, 'availability': 0, 'servicing': 0, 'reviews': 0, 'brand': 0, 'experience': 0}
    # check if any of the keywords appear in the specified columns
    for column in columns_to_search:
        for keyword in product_keywords:
            if keyword in str(row[column]):
                scores['product'] += 1
        for keyword in price_keywords:
            if keyword in str(row[column]):
                scores['price'] += 1
        for keyword in range_keywords:
            if keyword in str(row[column]):
                scores['range'] += 1
        for keyword in availability_keywords:
            if keyword in str(row[column]):
                scores['availability'] += 1
        for keyword in servicing_keywords:
            if keyword in str(row[column]):
                scores['servicing'] += 1
        for keyword in reviews_keywords:
            if keyword in str(row[column]):
                scores['reviews'] += 1
        for keyword in brand_keywords:
            if keyword in str(row[column]):
                scores['brand'] += 1
        for keyword in experience_keywords:
            if keyword in str(row[column]):
                scores['experience'] += 1
    # accumulate the scores for each category across all rows
    for category, score in scores.items():
        total_scores[category] += score

# print the total scores for each category
print(total_scores)

categories = list(total_scores.keys())
scores = list(total_scores.values())

# create a bar chart
plt.bar(categories, scores)

# add labels and title
plt.xlabel("Categories")
plt.ylabel("Scores")
plt.title("Sentiment Analysis Scores")

# display the chart
plt.show()