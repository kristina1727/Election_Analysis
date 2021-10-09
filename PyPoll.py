#  The data we need to retreive.
import csv
import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources","election_results.csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join("Analysis","election_analysis.txt")

# Create a variable to intitalize a total vote counter.
total_votes = 0

# Declare a new list - candidate options
candidate_options =[]

# Create a new dictionary with candidate name as the  key and votes as the value
candidate_votes = {}

# Declare a winning candidate variable to hold an empty string.
winning_candidate = ''

# Declare a variable for winning count set to zero
winning_count = 0

# Declare a variable for the winning percentage equal to zero.
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

# To do: read and analyze the data here
        
    # Read the header row
    headers = next(file_reader)
    #print(headers) 
    
    #print each row in the CSV file
    for row in file_reader:
       
        # Add to the total vote count.
        total_votes += 1

        #print the candidates name for each row.
        candidate_name = row [2]      
        
        # If the candidate does not match any existing candidate in the candidates list
        if candidate_name not in candidate_options:

           # Add it to the list of candidates by append the candidate_options list to include candidate_name
           candidate_options.append(candidate_name)

           # Begin tracking candidtes's vote count.
           candidate_votes[candidate_name] = 0

        #add a vote to that candidate's count
        candidate_votes[candidate_name]  += 1  
   
    # Determine the percentage of votes for each candidate by looping thorugh the counts.
    # Iterate through the candidate list.
    for candidate_name in candidate_options:

        # Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]

        # Calculate  the percent of total votes.
        vote_percentage = float(votes)/float(total_votes) * 100

        #print out each candidate's name, vote count and percentage of votes to the terminal
        print(f"{candidate_name}:  {vote_percentage:.1f}% ({votes:,})\n")

        # Determine winning vote count and candidate
        # Determine if the votes are greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            
            # If true then set the winning count = votes and winning percent =vote percentage
            winning_count = votes 
            winning_percentage = vote_percentage

            # Set the winning count equal to the candidate name
            winning_candidate = candidate_name
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Pergentage: {winning_percentage:.1f}\n"
        f"-------------------------\n")
    #Print out the winning candedidate, vote count and percentage to termina
    print(winning_candidate_summary)

# Print the candidate vote dictionary
#print(candidate_votes)

#3. Print the total votes
#print(total_votes)




# 1. The total number of votes cast
# 2. A complete list of candidates who  received votes
# 3. The percentage of votes each candidated won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote


# close the file.
#election_data.close()

#file_to_save = os.path.join("Analysis","election_analysis.txt")
#open(file_to_save, "w")



# Using the with statement open the file as a text file.
#with open(file_to_save,"w") as txt_file:    
    # Write some data to the file.
    # txt_file.write("Counties in the Election\n----------------------------\nArapahoe\nDenver\nJefferson")


    

