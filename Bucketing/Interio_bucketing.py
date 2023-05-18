import pandas as pd

# read the csv file into a pandas dataframe
df = pd.read_csv('./NLP/Interio.csv')

# define the lists of keywords for each category
product_keywords = ['design', 'modern', 'stylish', 'attractive', 'features', 'quality', 'durable', 'long lasting', 'material', 'innovation']
price_keywords = ['costly', 'high price', 'market pricing']
range_keywords = ['wide options']
availability_keywords = ['limited', 'online', 'offline', 'stores']
reviews_keywords = ['reviews', 'bad remarks']
servicing_keywords = ['servicing', 'customer service']
brand_keywords = ['brand', 'brand image', 'trust', 'legacy', 'heritage', 'reliable']
experience_keywords = ['experience', 'reviews', 'ratings', 'friends', 'family']


##  Product categorization

# define a function to check if any of the keywords are present in a given text
def check_keywords(text):
    if isinstance(text, str):
        for keyword in product_keywords:
            if keyword in text.lower():
                return True
    return False

# define a function to categorize the product based on the keywords and labeling
def categorize_product(row, product_keywords):
    if check_keywords(row['Interio-Text']):
        if row['Interio_label'] == 'Positive':
            return 'positive'
        elif row['Interio_label'] == 'Negative':
            return 'negative'
        else:
            return 'neutral'
    else:
        return None

# apply the categorize_product function to the dataframe
df['product'] = df.apply(categorize_product, args=(product_keywords,), axis=1)



##  Price categorization
# define a function to check if any of the keywords is present in a given text
def check_keywords_a(text):
    if isinstance(text, str):
        for keyword in price_keywords:
            if keyword in text.lower():
                return True
    return False

# define a function to categorize the price based on the keywords and labeling

def categorize_price(row1, price_keywords):
    if check_keywords_a(row1['Interio-Text']):
        if row1['Interio_label'] == 'Positive':
            return 'positive'
        elif row1['Interio_label'] == 'Negative':
            return 'negative'
        else:
            return 'neutral'
    else:
        return None

# apply the categorize_price function to the dataframe
df['price'] = df.apply(categorize_price, args=(price_keywords,), axis=1)




##  Range categorization
# define a function to check if any of the keywords are present in a given text
def check_keywords(text):
    if isinstance(text, str):
        for keyword in range_keywords:
            if keyword in text.lower():
                return True
    return False

# define a function to categorize the range based on the keywords and labeling
def categorize_range(row, range_keywords):
    if check_keywords(row['Interio-Text']):
        if row['Interio_label'] == 'Positive':
            return 'positive'
        elif row['Interio_label'] == 'Negative':
            return 'negative'
        else:
            return 'neutral'
    else:
        return None

# apply the categorize_range function to the dataframe
df['range'] = df.apply(categorize_range, args=(range_keywords,), axis=1)





##  Availability categorization
# define a function to check if any of the keywords are present in a given text
def check_keywords(text):
    if isinstance(text, str):
        for keyword in availability_keywords:
            if keyword in text.lower():
                return True
    return False

# define a function to categorize the availability based on the keywords and labeling
def categorize_availability(row, availability_keywords):
    if check_keywords(row['Interio-Text']):
        if row['Interio_label'] == 'Positive':
            return 'positive'
        elif row['Interio_label'] == 'Negative':
            return 'negative'
        else:
            return 'neutral'
    else:
        return None

# apply the categorize_availability function to the dataframe
df['availability'] = df.apply(categorize_availability, args=(availability_keywords,), axis=1)





##  Reviews categorization
# define a function to check if any of the keywords are present in a given text
def check_keywords(text):
    if isinstance(text, str):
        for keyword in reviews_keywords:
            if keyword in text.lower():
                return True
    return False

# define a function to categorize the reviews based on the keywords and labeling
def categorize_reviews(row, reviews_keywords):
    if check_keywords(row['Interio-Text']):
        if row['Interio_label'] == 'Positive':
            return 'positive'
        elif row['Interio_label'] == 'Negative':
            return 'negative'
        else:
            return 'neutral'
    else:
        return None

# apply the categorize_reviews function to the dataframe
df['reviews'] = df.apply(categorize_reviews, args=(reviews_keywords,), axis=1)





##  Servicing categorization
# define a function to check if any of the keywords are present in a given text
def check_keywords(text):
    if isinstance(text, str):
        for keyword in servicing_keywords:
            if keyword in text.lower():
                return True
    return False

# define a function to categorize the servicing based on the keywords and labeling
def categorize_servicing(row, servicing_keywords):
    if check_keywords(row['Interio-Text']):
        if row['Interio_label'] == 'Positive':
            return 'positive'
        elif row['Interio_label'] == 'Negative':
            return 'negative'
        else:
            return 'neutral'
    else:
        return None

# apply the categorize_servicing function to the dataframe
df['servicing'] = df.apply(categorize_servicing, args=(servicing_keywords,), axis=1)




##  Brand categorization
# define a function to check if any of the keywords are present in a given text
def check_keywords(text):
    if isinstance(text, str):
        for keyword in brand_keywords:
            if keyword in text.lower():
                return True
    return False

# define a function to categorize the brand based on the keywords and labeling
def categorize_brand(row, brand_keywords):
    if check_keywords(row['Interio-Text']):
        if row['Interio_label'] == 'Positive':
            return 'positive'
        elif row['Interio_label'] == 'Negative':
            return 'negative'
        else:
            return 'neutral'
    else:
        return None

# apply the categorize_brand function to the dataframe
df['brand'] = df.apply(categorize_brand, args=(brand_keywords,), axis=1)





##  Experience categorization
# define a function to check if any of the keywords are present in a given text
def check_keywords(text):
    if isinstance(text, str):
        for keyword in experience_keywords:
            if keyword in text.lower():
                return True
    return False

# define a function to categorize the experience based on the keywords and labeling
def categorize_experience(row, experience_keywords):
    if check_keywords(row['Interio-Text']):
        if row['Interio_label'] == 'Positive':
            return 'positive'
        elif row['Interio_label'] == 'Negative':
            return 'negative'
        else:
            return 'neutral'
    else:
        return None

# apply the categorize_experience function to the dataframe
df['experience'] = df.apply(categorize_experience, args=(experience_keywords,), axis=1)





# save the updated dataframe to a new csv file
df.to_csv('./Bucketing/Interio_bucketing.csv', index=False)
