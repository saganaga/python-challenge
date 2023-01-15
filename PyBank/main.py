# Modules
import os
import csv

# Variable declarations
total_months = 0

# Set path for file
csvpath = os.path.join(".", "Resources", "budget_data.csv")

# Open the CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # read the header row in first (store header row)
    csv_header = next(csvreader)

    row_count = 0
    for row in csvreader:

        # set row counter
        row_count = row_count + 1

    # assign total number of months in dataset
    total_months = row_count

print("Financial Analysis")
print("-" * 28)
print(f"Total Months: {row_count}")
