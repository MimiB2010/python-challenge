import os
import csv

#pull in the csv file 

budget_csv = os.path.join("..","Resources","budget_data.csv")

#read the csv file and skip the header row

month_count = 0
total_profit = 0
previous_profit = 0
profit_change = 0
   
greatest_increase = ["",0]
greatest_decrease = ["", 9999999999999999]
    
profit_changes = []

with open(budget_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader,None)
 
    #count the total number of months and total profit
       
    for row in csvreader:
        month_count = month_count + 1
        total_profit = total_profit + int(row[1])
        
    #net total of "Profit/Losses over the entire period"
        
        profit_change = int(row[1]) - previous_profit
        previous_profit = int(row[1])
        
        if (profit_change > greatest_increase[1]):
            greatest_increase[0] = row[0]
            greatest_increase[1] = profit_change
            
        if (profit_change < greatest_decrease[1]):
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = profit_change
        
        profit_changes.append(int(row[1]))
    
    profit_average = sum(profit_changes) / len(profit_changes)
    print(profit_average)
            
    
    print("Financial Analysis")
    print("-----------------------------------")
    print(f"Total Months: {month_count}")
    print(f"Total: ${total_profit}")
    print("Average Change: " + "$" + str(round(sum(profit_changes) / len(profit_changes),2)))
    print("Greatest Increase in Profits:" + str(greatest_increase[0]) + "($" + str(greatest_increase[1]) + ")")
    print("Greatest Decrease in Profits:" + str(greatest_decrease[0]) + "($" + str(greatest_decrease[1]) + ")")

output = os.path.join("bank_analysis.txt")

with open("bank_analysis.txt","w") as text_file:
    print("Financial Analysis", file=text_file)
    print("-----------------------------------", file=text_file)
    print(f"Total Months: {month_count}", file=text_file)
    print(f"Total: ${total_profit}", file=text_file)
    print("Average Change: " + "$" + str(round(sum(profit_changes) / len(profit_changes),2)), file=text_file)
    print("Greatest Increase in Profits:" + str(greatest_increase[0]) + "($" + str(greatest_increase[1]) + ")", file=text_file)
    print("Greatest Decrease in Profits:" + str(greatest_decrease[0]) + "($" + str(greatest_decrease[1]) + ")", file=text_file)

with open("bank_analysis.txt","r")as text_file2:
    print(text_file2.read())
