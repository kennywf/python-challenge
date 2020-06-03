# import modules
import os 
import csv

# declare variables 
votes = []
total_votes = 0
candidate_list = []
candidates_total = []
percentage = []

# set path for file .csv file
csvpath = os.path.join('Resources','election_data.csv')

# open the .csv 
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # read the header row first 
    csv_header = next(csvreader)
    print(f"Header: {csv_header}")

    #start loop
    for row in csvreader:

        # count total number of votes
        total_votes = total_votes + 1

        # set candidates to r[2]
        candidate = row [2]

        # candidate list and vote count get from r[2]
        if candidate not in candidate_list:
            candidate_list.append(candidate)

        # vote list
        votes.append(candidate)

    
    # second loop through the candidates and votes with previously obtained values
    # candidates_total.append adds each vote for candidates by using the .count function 
    # percentage.append adds the percentage value for each candidate, round( ,) used to round decimals  
    for candidate in candidate_list:
        candidates_total.append(votes.count(candidate))
        percentage.append(100 * (votes.count(candidate)) / (total_votes))

# declare variables to get winning candidate 
highest_votes = candidates_total[0]
max_candidate = 0

# run loop through list of candidates to look for candidate with highest votes
for x in range(len(candidate_list)):
        if candidates_total[x] > highest_votes:
            highest_votes = candidates_total[x]
            max_candidate = x
winner = candidate_list[max_candidate]

# print to terminal     
print(f'Election Results \n')
print(f'------------------------------------\n')
print(f'Total Votes: {total_votes} \n') 
print(f'------------------------------------\n')

# initialize a printing loop where i are the candidates in the list     
for i in range(len(candidate_list)):
    print("{}: {:.3f}% ({})".format(candidate_list[i], percentage[i], candidates_total[i]))
print(f'------------------------------------\n')
print(f'Winner: {winner}')
print(f'------------------------------------\n')

#export file to .txt 
analysis_file = os.path.join('analysis', 'analysis.txt')
with open(analysis_file, "w") as output:
    output.write(f'Election Results \n')
    output.write(f'------------------------------------\n')
    output.write(f'Total Votes: {total_votes} \n') 
    output.write(f'------------------------------------\n')
    for i in range(len(candidate_list)):
        output.write("{}: {:.3f}% ({})\n".format(candidate_list[i], percentage[i], candidates_total[i]))
    output.write(f'------------------------------------\n')
    output.write(f'Winner: {winner}\n')
    output.write(f'------------------------------------\n')
