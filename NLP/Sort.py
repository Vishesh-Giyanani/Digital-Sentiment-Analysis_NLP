import csv
import pandas as pd

# Open the CSV file and create a csv.reader object
with open('./NLP/Final2.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)

    # Create a new list to store the rearranged data
    new_data = []

    # Loop through the rows of the csv.reader object and rearrange the columns
    for row in reader:
        new_row = [row[0], row[1], row[2], row[3], row[4], row[5], row[22], row[23], row[24], row[34], row[6], row[7], row[25], row[26], row[27], row[35], row[8], row[9], row[28], row[29], row[30], row[36], row[10], row[11], row[31], row[32], row[33], row[37], row[12], row[13], row[14], row[15], row[16], row[17], row[18], row[19], row[20], row[21]]
        new_data.append(new_row)

# Close the CSV file
csv_file.close()

# Open the same CSV file again and create a csv.writer object
with open('./NLP/Final2.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)

    # Loop through the rows of the new list and write each row to the CSV file
    for row in new_data:
        writer.writerow(row)

df = pd.DataFrame(new_data)

# Write the updated DataFrame to a new csv file
df.to_csv('./NLP/C.csv', index=False)