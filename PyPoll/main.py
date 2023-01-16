# Modules
import os
import csv

# Variable declarations
total_votes = 0

# Set path for file
csvpath = os.path.join(".", "Resources", "election_data.csv")

# Open the CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row in first (store header row)
    csv_header = next(csvreader)

    row_count = 0

    for row in csvreader:

            # set row counter
            row_count = row_count + 1

# assign total number of votes in dataset
    total_votes = row_count

# Print to Terminal
print("Election Results")
print("-" * 25)
print(f"Total Votes: {row_count}")
print("-" * 25)
print(f"Charles Casper Stockham: ")
print(f"Diana DeGette: ")
print(f"Raymon Anthony Doane: ")
print("-" * 25)
print(f"Winner: ")
print("-" * 25)

# Specify the file to write to
output_path = os.path.join(".", "analysis", "output.txt")

# Open the file using "write" mode. Specify the variables to hold the contents
with open(output_path, 'w') as output:
    print("Election Results", file = output)
    print("-" * 25, file = output)
    print(f"Total Votes: {row_count}", file = output)
    print("-" * 25, file = output)
    print(f"Charles Casper Stockham: ", file = output)
    print(f"Diana DeGette: ", file = output)
    print(f"Raymon Anthony Doane: ", file = output)
    print("-" * 25, file = output)
    print(f"Winner: ", file = output)
    print("-" * 25, file = output)
