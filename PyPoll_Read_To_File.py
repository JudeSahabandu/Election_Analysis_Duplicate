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
file_to_save = os.path.join("Analysis", "election_analysis.txt")

# 1. Initialize a total vote counter
total_votes = 0

# 2. Declare candidate options list
candidate_options = []

# 3. Declare the empty dictionary.
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Read the header row
    headers = next(file_reader)

# Print each row in the CSV file.
    for row in file_reader:
        # Add the total vote count
        total_votes += 1

        # Print the candidate name from each row
        candidate_name = row[2]

# If candidate name does not match any existing options
        if candidate_name not in candidate_options:
            
            # Add the candidate options to the list
            candidate_options.append(candidate_name)

            # 2. Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

        # Save the results to our text file
        with open(file_to_save, "w") as txt_file:

# Determine the percentage of votes for each candidate by looping through the counts.
# 1. Iterate through the candidate list
            for candidate_name in candidate_votes:

                # 2. Retreive vote count of a candidate
                votes = candidate_votes[candidate_name]

                # 3. Calculate the percentage of votes.
                vote_percentage = float(votes)/float(total_votes) * 100

                #  To do: print out each candidate's name, vote count, and percentage of
                # votes to the terminal.
                #print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

                # Determine winning vote count and candidate
                # Determine if the votes is greater than the winning count.
                if (votes > winning_count) and (vote_percentage > winning_percentage):
                    # If true then set winning_count = votes and winning_percent =
                    # vote_percentage.
                    winning_count = votes
                    winning_percentage = vote_percentage
                    # And, set the winning_candidate equal to the candidate's name.
                    winning_candidate = candidate_name

            # Print the final vote count to the terminal.
            election_results = (
            f"\nElection Results\n"
            f"-------------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"-------------------------\n")
            print(election_results, end="")
            # Save the final vote count to the text file.
            txt_file.write(election_results)

            #winning_candidate_summary = (
            #    f"-------------------------\n"
            #    f"Winner: {winning_candidate}\n"
            #    f"Winning Vote Count: {winning_count:,}\n"
            #    f"Winning Percentage: {winning_percentage:.1f}%\n"
            #    f"-------------------------\n")
#print(winning_candidate_summary)

#  To do: print out the winning candidate, vote count and percentage to
#   terminal.



# Print the candidate vote dictionary.
#print(candidate_votes)

# Print the total votes
#print(total_votes)

# Print the candidate options
#print(candidate_options)

# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote