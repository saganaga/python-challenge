# Modules
import os
import csv

# Variable declarations
total_months = 0
total = 0
changes = list()

# Set path for file
csvpath = os.path.join(".", "Resources", "budget_data.csv")

# Open the CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # read the header row in first (store header row)
    csv_header = next(csvreader)

    row_count = 0

    # prev_pl is previous row Profit/Losses value
    prev_pl = None

    for row in csvreader:

        # set row counter
        row_count = row_count + 1

        # current_pl is current row Profit/Losses value
        current_pl = int(row[1])

        # assign total amount of Profit/Losses, convert to integer
        total = total + current_pl

        if prev_pl is not None:
            change = current_pl - prev_pl  
            changes.append(change)

        # store the current_pl so that in the next iteration in the loop it becomes the prev_pl
        prev_pl = current_pl

    # assign total number of months in dataset
    total_months = row_count

print("Financial Analysis")
print("-" * 28)
print(f"Total Months: {row_count}")
print("Total: $" + str(total))
print(f"Average Change: ${round(sum(changes)/len(changes),2)}")
print(f"Greatest Increase in Profits: (date TODO) (${max(changes)})")
print(f"Greatest Decrease in Profits: (date TODO) (${min(changes)})")
