# import csv file
import os
import csv
import statistics as stats
import math 
import numpy as np


csvpath= os.path.join('election_data.csv')

with open(csvpath, "r", newline="") as archivito:
        csvreader = csv.reader(archivito, delimiter=",")
        csv_header = next(csvreader)

        voter_id_list = []
        county_list = []
        candidate_list = []
        
        for row in csvreader:
                voter_id = (row[0])
                county = (row[1])
                candidate= (row[2])
                voter_id_list.append(voter_id)
                county_list.append(county)
                candidate_list.append(candidate)

        # total_voters = sum(voter_id_list)
        # print(f'Total number of voters is {total_voters}')
        
print ("                  ")
print ("Election Results")
print ("----------------")

total_voters = len(voter_id_list)
print("Total number of voters is: ", total_voters)
print ("----------------")


#calculate votes of each candidates

Khan = candidate_list.count("Khan")
khan_percentage = (Khan/total_voters)*100
print("Khan: ",khan_percentage,"%", "(",Khan, ")")

Correy = candidate_list.count("Correy")
correy_percentage = (Correy/total_voters)*100
print("Correy: ",correy_percentage,"%", "(",Correy, ")")

Li = candidate_list.count("Li")
li_percentage = (Li/total_voters)*100
print("Li: ",li_percentage,"%", "(",Li, ")")

Tooley = candidate_list.count("O'Tooley")
tooley_percentage = (Tooley/total_voters)*100
print("O'Tooley: ",tooley_percentage,"%", "(",Tooley, ")")

# if statements to identify and print winner candidate

print(   )

if Khan > Correy and Khan > Li and Khan > Tooley:
        print( "Winner: Khan!")

elif Correy > Li and Correy > Tooley:
        print ("Winner: Correy!")

elif Li > Tooley:
        print ("Winner: Li!")

else:
        print("Winner: O'Tooley!")


