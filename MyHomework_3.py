# touch first_file.py will create a file

# Store the file path associated with the file (note the backslash may be OS specific)
#file = '../Resources/input.txt'

#Import the os module
import os

# Import module for reading CSV files
import csv

# Path to collect data from the Resources folder
csvpath = "Resources/budget_data.csv"

# Read in the CSV file
with open(csvpath, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first 
    csv_header = next(csvreader)
    
    #The total number of months included in the dataset
    row_count = 0
    #csvfile.seek(0)
    #next(csvreader)

    

    #The total net amount of "Profit/Losses" over the entire period
    sum_profit = 0
    sum_loss = 0
    totalPL = 0
    profit = 0

    for row in csvreader:
        row_count = row_count + 1
        profit = profit + int(row[1])
        if profit > 0:
            sum_profit = sum_profit + profit
        elif profit < 0:
            sum_loss = sum_loss + profit
    totalPL = sum_profit - sum_loss  
    print ("Financial Analysis")
    print ("---------------------------------------")
    print (f"Total Months : {row_count}" )
    print (f"Total : {totalPL}")

    #The average change in "Profit/Losses" between months over the entire period
    previous = 0
    current = 0
    chngPL = 0
    change = 0
    

with open(csvpath, 'r') as csvfile:
    max = 0
    min = 0
    changelist = []
    monthlist = []
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    for row in csvreader:
        #Smonths = int(row[0])
        previous = int(row[1])
        current = previous + int(row[1])
        change = (current - previous)
        changelist.append(change)
        if max < change: 
            max = change
        if min > change:
            min = change
    chngPL = sum(changelist)/len(changelist)
    print (f"Average Change : {chngPL}")
    print (f"Greatest Increase in Profits: {max}")
    print (f"Greatest Decrease in Profits: {min}")


    #for x in range(row[2]):
    #print(x


    #The greatest increase in profits (date and amount) over the entire period
    
    #The greatest decrease in losses (date and amount) over the entire period
    #min(change)