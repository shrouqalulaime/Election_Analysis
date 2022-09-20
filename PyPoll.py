
#Import Dependencies
import os
import csv

#file path we will read
file_to_load=os.path.join("Resources", "election_results.csv")

#file path we will save
file_to_save=os.path.join("analysis", "election_analysis.txt")


with open(file_to_load) as election_data:
    #read data with csv
    file_reader=csv.reader(election_data)

    #skip header row
    headers=next(file_reader)
    
    
    total_votes=0
    candidate_options=[]
    candidate_vote={}

    for row in file_reader:
        #The total number of votes cast
        total_votes+=1

        #A complete list of candidates who recived votes
        candidate=row[2]
        if candidate not in candidate_options:
            candidate_options.append(candidate)

            #add candiadte to the dictionary
            candidate_vote[candidate]=0

        #The total number of votes each candidate won
        candidate_vote[candidate]+=1

    
print(total_votes)
print(candidate_options)
print(candidate_vote)


winning_candidate = ""
winning_count = 0
winning_percentage = 0
 #The percentage of votes each candidate won   
for candidate_name in candidate_vote:
    votes=candidate_vote[candidate_name]
    vote_percentage=float(votes)/float(total_votes)*100

    ##The winner of the election based on popular vote
    if (votes>winning_count) and (vote_percentage>winning_percentage):
        winning_count=votes
        winning_percentage=vote_percentage
        winning_candidate=candidate_name
    print(f"{candidate_name}: {vote_percentage: .2f}% ({votes:,})\n")

winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)