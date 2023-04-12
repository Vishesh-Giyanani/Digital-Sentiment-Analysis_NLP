import pandas as pd

# read the CSV file into a DataFrame
df = pd.read_csv("./NLP/Final3.csv")
 
# define the columns to search
columns_to_search = ["Appliances-Text", "Locks-Text", "Interio-Text", "Security-Text"]

# define the lists of keywords for each category
product_keywords = ['design', 'modern', 'stylish', 'attractive', 'features', 'quality', 'durable', 'long lasting', 'material', 'innovation']
price_keywords = ['costly', 'high price', 'market pricing']
range_keywords = ['wide options']
availability_keywords = ['limited', 'online', 'offline', 'stores']
servicing_keywords = ['servicing', 'customer service']
reviews_keywords = ['reviews', 'bad remarks']
brand_keywords = ['brand', 'brand image', 'trust', 'legacy', 'heritage', 'reliable']
experience_keywords = ['experience', 'reviews', 'ratings', 'friends', 'family']

# loop through each row in the DataFrame
for i, row in df.iterrows():
    # initialize a dictionary to store the scores for each category
    scores = {'product': 0, 'price': 0, 'range': 0, 'availability': 0, 'servicing': 0, 'reviews': 0, 'brand': 0, 'experience': 0}
    # check if any of the keywords appear in the specified columns
    for column in columns_to_search:
        for keyword in product_keywords:
            if keyword in row[column]:
                scores['product'] += 1
        for keyword in price_keywords:
            if keyword in row[column]:
                scores['price'] += 1
        for keyword in range_keywords:
            if keyword in row[column]:
                scores['range'] += 1
        for keyword in availability_keywords:
            if keyword in row[column]:
                scores['availability'] += 1
        for keyword in servicing_keywords:
            if keyword in row[column]:
                scores['servicing'] += 1
        for keyword in reviews_keywords:
            if keyword in row[column]:
                scores['reviews'] += 1
        for keyword in brand_keywords:
            if keyword in row[column]:
                scores['brand'] += 1
        for keyword in experience_keywords:
            if keyword in row[column]:
                scores['experience'] += 1
    # add the scores as new columns to the DataFrame
    for category, score in scores.items():
        df.at[i, category] = score

# display the DataFrame with the new columns
print(df)
