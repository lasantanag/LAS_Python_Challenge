# import csv file
import os
import csv
import statistics as stats
import math 
import numpy as np

print ("                  ")
print ("Financial Analysis")
print ("----------------")

csvpath= os.path.join('budget_data.csv')

with open(csvpath, "r", newline="") as archivito:
        csvreader = csv.reader(archivito, delimiter=",")
        csv_header = next(csvreader)

        month_list = []
        profit_losses_list = []
        
        for row in csvreader:
                month = (row[0])
                month_list.append(month)
                Profit_Losses=(int(row[1]))
                profit_losses_list.append(Profit_Losses)

        total = sum(profit_losses_list)
        print(f'total profit is {total}')


number_of_months = len(profit_losses_list)
print("Total Months: ", number_of_months)

month_difference = np.diff(profit_losses_list)
print ("Average Change: $", stats.mean(month_difference))

max_increase = max(month_difference)
max_decrease = min(month_difference)

convertion_to_list = list(month_difference)

index_max_increase = convertion_to_list.index(max_increase) +1
index_max_decrease = convertion_to_list.index(max_decrease) +1 

#print({month_list [index_max_increase]})
#print({month_list [index_max_decrease]})

print ("Greatest Increase in Profits: ", {month_list [index_max_increase]},"$ ", max_increase)
print ("Greatest decrease in Profits: ", {month_list [index_max_decrease]},"$ ", max_decrease)

print ("Thanks!")