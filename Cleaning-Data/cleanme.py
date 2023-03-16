import pandas as pd
import re

# Define the strategies for handling null values and gibberish data
null_strategy = "delete"  # replace with "default" or "interpolate" as needed
gibberish_strategy = "delete"  # replace with "standardize" or "default" as needed

# Read the CSV file into a pandas dataframe
df = pd.read_csv("first.csv")

# Scrub the "B2_1L" column
if null_strategy == "delete":
    df = df.dropna(subset=["B2_1L"])
elif null_strategy == "default":
    df["B2_1L"] = df["B2_1L"].fillna("default_value")
elif null_strategy == "interpolate":
    df["B2_1L"] = df["B2_1L"].interpolate()

if gibberish_strategy == "delete":
    df["B2_1L"] = df["B2_1L"].apply(lambda x: re.sub(r'[^a-zA-Z0-9\s]', '', x))
elif gibberish_strategy == "standardize":
    df["B2_1L"] = df["B2_1L"].apply(lambda x: re.sub(r'[^a-zA-Z0-9\s]', ' ', x))

# Write the scrubbed data to a new CSV file
df.to_csv("second.csv", index=False)

