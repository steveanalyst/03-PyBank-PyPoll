import os
import csv

# input and output files
input_file = '/Users/wheat/python3/PyPoll/Resources/election_data.csv'
output_file = '/Users/wheat/python3/PyPoll/Resources/election_summary.txt'

#define all needed lists here
candidates, total_candidates, candidate_pct, candidate_total_count, summaries = ([] for _ in range(5))

# read in data from file
with open(input_file, mode='r', newline='') as poll_result:
    reader = csv.reader(poll_result, delimiter=',')

    next(reader)

    num_rows = 0

    for row in reader:
        total_candidates.append(row[2])
        num_rows += 1


# sorted list of total_candidates
sorted_candidates = sorted(total_candidates)

#get unique candidates data and save into candidates list
for i in range(num_rows):
    #if the current candidate is different than previous one, add it to the unique list
    if sorted_candidates[i - 1] != sorted_candidates[i]:
        candidates.append(sorted_candidates[i])

#print the summary header and total votes
print("\nElection Results")
print("-" * 25)
print("Total Votes:", num_rows)
print("-" * 25)


#count total voting for each candidate
for j in range(len(candidates)):
    candidate_count = 0

    for k in range(len(sorted_candidates)):
        if candidates[j] == sorted_candidates[k]:
            candidate_count += 1
    
    #get percentage number added with 3 decimal places
    candidate_pct.append(format((candidate_count / num_rows * 100), '.3f'))
    candidate_total_count.append(candidate_count)

# Zip all three lists together into tuples and sorted by percentage descending
candidate_info = sorted(zip(candidates, candidate_pct, candidate_total_count),key=lambda x:x[-1],reverse=True)



#create candidate info for name, voting % and total voting count and print out
for col in candidate_info:
    print(col[0] + ":", str(col[1]) + "%", "(" + str(col[2]) + ")")
    summary = (col[0] + ":", str(col[1]) + "%", " (" + str(col[2]) + ")")
    summaries.append(summary)

#find winner based on total count
for k in range(len(candidate_pct)):
    if candidate_total_count[k] > candidate_total_count[k - 1]:
        election_winner = candidates[k]


        
# Print winner result to terminal

print("-" * 25)
print("Winner:", election_winner)
print("-" * 25)
print("\n\n")

# Print result to file
with open(output_file, mode='w',newline='') as election_summaries:
    writer = csv.writer(election_summaries)

    writer.writerows([
        ["Election Results"],
        ["-" * 30],
        ["Total Votes: " + str(num_rows)],
        ["-" * 30]
    ])
    
    
    writer.writerows(summaries)
    
        
    writer.writerows([
        ["-" * 30],
        ["Winner: " + str(election_winner)],
        ["-" * 30]
    ])


