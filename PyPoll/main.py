import os
import csv
from operator import itemgetter

election_csv = os.path.join("..","Resources","election_data.csv")

total_votes = 0
total_candidates = 0
votes_won = 0
candidate_names = []
candidate_votes = {}

with open(election_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader,None)
    
    for row in csvreader:
        total_votes = total_votes + 1
        total_candidates = row[2]
        
        if row[2] not in candidate_names:
            candidate_names.append(row[2])
            candidate_votes[row[2]] = 1
        else:
            candidate_votes[row[2]] = candidate_votes[row[2]] + 1
        
                  
    print("Election Results")
    print("------------------------")
    print(f"Total Votes: {total_votes}")
    print("------------------------")
    
    for candidate in candidate_votes:
        print(candidate + " " + str(round(((candidate_votes[candidate]/total_votes)*100))) + "%" + " " + "(" + str(candidate_votes[candidate]) + ")")
        candidate_results = (candidate + " " + str(round(((candidate_votes[candidate]/total_votes)*100))) + "%" + "(" + str(candidate_votes[candidate]) + ")")   

candidate_votes
winner = sorted(candidate_votes.items(), key=itemgetter(1), reverse=True)
    
print("------------------------")
print("Winner: " + str(winner[0]))
print("------------------------")

output = os.path.join("poll_data.txt")

with open ("poll_data.txt","w") as text_file:
    print("Election Results", file=text_file)
    print("------------------------", file=text_file)
    print(f"Total Votes: {total_votes}", file=text_file)
    print("------------------------", file=text_file)
    
    for candidate in candidate_votes:
        print(candidate + " " + str(round(((candidate_votes[candidate]/total_votes)*100),3)) + "%" + " " + "(" + str(candidate_votes[candidate]) + ")", file=text_file)
        candidate_results = (candidate + " " + str(round(((candidate_votes[candidate]/total_votes)*100),3)) + "%" + "(" + str(candidate_votes[candidate]) + ")")
        
    candidate_votes
    winner= sorted(candidate_votes.items(), key=itemgetter(1), reverse=True)

    print("------------------------", file=text_file)
    print("Winner: " + str(winner[0]), file=text_file)
    print("------------------------", file=text_file)
    
with open ("poll_data.txt","r") as text_file2:
    print(text_file2.read())