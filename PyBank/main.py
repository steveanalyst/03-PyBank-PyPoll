# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

#setup file with path
csvpath="/Users/wheat/Documents/SMDA201811DATA2/03-HWSubmission/03-Python/PyBank/Resources/budget_data.csv"

#this waiting to be fixed
df = pd.read_csv(csvpath)
total = df['Profit/Losses'].sum()

csvfile = open(csvpath, newline='')
csvreader = csv.reader(csvfile)
changeList = []
for i, n in enumerate(csvreader):
    changeList.append(int(n[1])
change = 0
for num in changeList:
    change = num[1]-num[0]


# Reading using CSV module

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    
    #since each row is unique, it will be the Total Months Count
    row_count = sum(1 for row in csvreader) 

#Print the final report
print ("Financial Analysis")
print("--------------------------")
print("Total Months:", row_count)
print("Total:", '${}'.format(total))