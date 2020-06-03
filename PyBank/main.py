# import modules 
import os 
import csv 

# variables
months = 0
net_amount = 0
prev_month= 0
current_month = 0
average_change = 0
revenue_change = 0
greatest_increase = 0
greatest_decrease = 0
greatest_increase_month = ""
greatest_decrease_month = ""


# set path for file .csv file
csvpath = os.path.join('Resources','budget_data.csv')

# open the .csv 
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # read the header row first 
    csv_header = next(csvreader)
    print(f"Header: {csv_header}")

    #start loop
    for row in csvreader:

        # calculate total month in dataset (use += to add the next row)
        months += 1
        
        # calculate net amount or revenue (row[1] sum of loss and profits)
        net_amount = net_amount + int(row[1])

        # set revenue = profit - previous months profit where previous month profit starts at 0 
        revenue = int(row[1]) - prev_month
        
        # calculate net change in revenue
        if months != 1:
            revenue_change = revenue_change + revenue
        
        # calculation for greatest revenue increase - use row[0] to get exact date.
        if (revenue > greatest_increase):
            greatest_increase = revenue
            greatest_increase_month = row[0]

        # calculation for greatest revenue decrease - use row[0] to get exact date.
        elif (revenue < greatest_decrease):
            greatest_decrease = revenue
            greatest_decrease_month = row[0]
        
        #set previous month profit to current before the start of new loop
        prev_month = int(row[1])

    #calculate average change     
    average_change = revenue_change / (months - 1)

    #print financial analysis 
    print("Financial Analysis")
    print("-------------------------------------------------")
    print(f"Total Months: {months}")
    print(f"Total: ${net_amount}")
    print(f"Average Change: ${round(average_change,2)}")
    print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})")
    print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})")       
    
#export file to .txt 
analysis_file = os.path.join('analysis', 'analysis.txt')
with open(analysis_file, "w") as output:
    output.write("Financial Analysis\n")
    output.write("-------------------------------------------------\n")
    output.write(f"Total Months: {months}\n")
    output.write(f"Total: ${net_amount}\n")
    output.write(f"Average Change: ${round(average_change,2)}\n")
    output.write(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n")
    output.write(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})\n")    

