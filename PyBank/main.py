import os
import csv

date, profit = ([] for i in range(2))

# input and output files
input_file = "/Users/wheat/python3/PyBank/Resources/budget_data.csv"
output_file = "/Users/wheat/python3/PyBank/Resources/budget_data_summary.txt"


with open(input_file, newline='') as budget_data:
    
    # CSV reader specifies delimiter and variable that holds contents
    reader = csv.reader(budget_data, delimiter=',')

    # skip the header row
    next(reader)

    row_num = 0
    for row in reader:
        date.append(row[0])
        profit.append(row[1])
        row_num += 1


# print summary header and dividing lines
print("\nFinancial Analysis", "\n" + "-" * 30)

# month count
print("Total Months:", row_num)


# calculate the total profit
profit_sum = 0
for i in profit:
    profit_sum += int(i)

print("Total: $" + str(profit_sum))


# average change
total_change = 0
for c in range(row_num):
    total_change += (int(profit[c-1]) - int(profit[c]))
    
# get the first number in the list and deducted from the total change
first_number = (int(profit[0]) - int(profit[-1]))
final_total_change = total_change - first_number

avg_change = final_total_change / ((row_num)-1)


print("Average Change: $" + str("{:.2f}".format(avg_change)))


# greatest increase in profit
max_increase = 0
for m in range(len(profit)):
    if int(profit[m]) - int(profit[m - 1]) > max_increase:
        max_increase = int(profit[m]) - int(profit[m - 1])
        max_increase_month = date[m]

print("Greatest Increase in Profits:", max_increase_month, "($" + str(max_increase) + ")")


# greatest decrease in profit
max_decrease = 0
for n in range(len(profit)):
    if int(profit[n]) - int(profit[n - 1]) < max_decrease:
        max_decrease = int(profit[n]) - int(profit[n - 1])
        max_decrease_month = date[n]

print("Greatest Decrease in Profits:", max_decrease_month, "($" + str(max_decrease) + ")")



# Output data as a text file 
with open(output_file, mode='w', newline='') as summary_txt:
    writer = csv.writer(summary_txt)

    writer.writerows([
        ["Financial Analysis" ],
        ["-" * 30],
        ["Total Months: " + str(row_num)],
        ["Total: $" + str(profit_sum)],
        ["Average Change: $" + str("{:.2f}".format(avg_change))],
        ["Greatest Increase in Profits: " + str(max_increase_month) + " ($" + str(max_increase) + ")"],
        ["Greatest Decrease in Profits: " + str(max_decrease_month) + " ($" + str(max_decrease) + ")"]
    ])
