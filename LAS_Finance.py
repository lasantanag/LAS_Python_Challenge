# import csv file
import os
import csv

csvpath= os.path.join('LAS_Python_Finance.csv')

with open(csvpath, newline='') as csvfile:
        csvreader=csv.reader(csvfile,delimiter=',')
        print(csvreader)
        csv_header=next(csvreader)
        print(f"csv header: {csv_header}")
        # for row in csvreader:
        #         print(row)

        row_count = sum(1 for row in csvreader)
        print(row_count)
        
        total = sum(int([1]) for row in csvreader)
        print(total)

       
       
