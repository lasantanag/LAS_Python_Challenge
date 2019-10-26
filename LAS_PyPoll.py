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
        
print ("Election Results")
print ("----------------")

total_voters = len(voter_id_list)
print("Total number of voters is: ", total_voters)
print ("----------------")
