import os
import csv

month_count=[]
net_total=[]
average_change=[]

#pull in the budget data csv file
bank_csv=os.path.join("..","Resources","budget_data.csv")

#read the csv file
with open(bank_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
#skip the header row
