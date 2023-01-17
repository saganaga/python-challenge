# Modules
import os
import csv

# Variable declarations
total_votes = 0
candidate_vote_totals = dict()

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

            candidate = row[2]
            # Is the candidate in the dictionary?
            if candidate in candidate_vote_totals:
                # If yes, then add one vote
                candidate_vote_totals[candidate] = candidate_vote_totals[candidate] + 1
            else:
                # Otherwise add them to the dictionary with a vote count of 1
                candidate_vote_totals[candidate] = 1

# assign total number of votes in dataset
total_votes = row_count

# Print to Terminal
print("Election Results")
print("-" * 25)
print(f"Total Votes: {total_votes}")
print("-" * 25)
winner = None
max_votes = 0

for candidate in candidate_vote_totals.keys():
    votes = candidate_vote_totals[candidate]
    percent = (100.0*votes)/total_votes
    print(f"{candidate}: {percent:.3f}% ({votes})")
    if votes > max_votes:
        winner = candidate
        max_votes = votes
print("-" * 25)
print(f"Winner: {winner}")
print("-" * 25)

# Specify the file to write to
output_path = os.path.join(".", "analysis", "output.txt")

# Open the file using "write" mode. Specify the variables to hold the contents
with open(output_path, 'w') as output:
    print("Election Results", file = output)
    print("-" * 25, file = output)
    print(f"Total Votes: {total_votes}", file = output)
    print("-" * 25, file = output)
    for candidate in candidate_vote_totals.keys():
        votes = candidate_vote_totals[candidate]
        percent = (100.0*votes)/total_votes
        print(f"{candidate}: {percent:.3f}% ({votes})", file = output)
    print("-" * 25, file = output)
    print(f"Winner: {winner}", file = output)
    print("-" * 25, file = output)
