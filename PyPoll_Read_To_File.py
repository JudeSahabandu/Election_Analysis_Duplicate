# The data we need to retreive

# Direct Method to open a file
# Assign a variable for the file to load and the path.
#file_to_load = 'Resources/election_results.csv'

# Open the election results and read the file.
#election_data = open(file_to_load, 'r')

# To do: perform analysis.
#print(election_data)

# Close the file.
#election_data.close()


# Indirect Method to open a file
import os
import csv

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join("Analysis", "election_results.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

 # Print each row in the CSV file.
    for row in file_reader:
        print(row)

 # Print the headers in the CSV file.
    #headers = next(file_reader)
    #print(headers)


# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote