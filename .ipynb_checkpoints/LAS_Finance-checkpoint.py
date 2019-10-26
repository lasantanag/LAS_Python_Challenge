# import csv file
import os
import csv

csvpath= os.path.join('LAS_Python_Finance.csv')

with open(csvpath, newline='') as archivito:
        csvreader=csv.reader(archivito,delimiter=',')
        print(csvreader)
        csv_header=next(csvreader)
        print(f"csv header: {csv_header}")
        # for row in csvreader:
        #         print(row)

        row_count = sum(1 for row in csvreader)
        print(row_count)
        
        total = sum(int(row([1])) for row in next.csvreader
        print (total)
 
       
       
