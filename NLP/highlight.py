import csv
from openpyxl import Workbook
from openpyxl.styles import PatternFill

# Read the input CSV file
with open('./NLP/final3.csv', 'r') as infile:
    reader = csv.reader(infile)
    data = [tuple(row) for row in reader]

# Create a new workbook and select the active worksheet
workbook = Workbook()
worksheet = workbook.active

# Define the column numbers you want to sort and the order to use
columns_to_sort = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27]
sort_order = {'Positive': 1, 'Neutral': 2, 'Negative': 3}

# Sort the data by the selected columns and sort order
data.sort(key=lambda row: [sort_order.get(row[col], 0) for col in columns_to_sort])

# Define the column numbers you want to highlight and the colors to use
columns_to_highlight = {4: 'FFC0CB', 5: 'FFC0CB', 6: 'FFC0CB', 7: 'FFC0CB', 8: 'FFC0CB', 9: 'FFC0CB',
                        10: 'ADD8E6', 11: 'ADD8E6', 12: 'ADD8E6', 13: 'ADD8E6', 14: 'ADD8E6', 15: 'ADD8E6',
                        16: '98FB98', 17: '98FB98', 18: '98FB98', 19: '98FB98', 20: '98FB98', 21: '98FB98',
                        22: 'E6E6FA', 23: 'E6E6FA', 24: 'E6E6FA', 25: 'E6E6FA', 26: 'E6E6FA', 27: 'E6E6FA'}

# Iterate through the keys of columns_to_highlight and apply the fill style to the cells in each column
for col_num in columns_to_highlight.keys():
    color = columns_to_highlight[col_num]
    fill = PatternFill(start_color=color, end_color=color, fill_type='solid')
    for row_num, row in enumerate(data, start=1):
        cell = worksheet.cell(row=row_num, column=col_num)
        cell.value = row[col_num - 1]
        cell.fill = fill

# Write the output to a new CSV file
with open('./NLP/final4.csv', 'w', newline='') as outfile:
    writer = csv.writer(outfile)
    for row in data:
        writer.writerow(row)

workbook.save('./NLP/final4.xlsx')