# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 15:51:24 2019

@author: ai3ca
"""


import os
import csv


election_data_csv = os.path.join("election_data.csv")


voter_id=[]
vote_per_candidate=[]
candidate=[]
unique_candidate=[]
vote_percent=[]


with open(election_data_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    for row in csvreader:
    
        candidate.append(row[2])
        
        voter_id.append(row[0])
    vote=len(voter_id)        
    for x in set(candidate): #set():an unordered collection with no duplicate elements
        unique_candidate.append(x)
        y=candidate.count(x)
        vote_per_candidate.append(y)
        z=(y/vote)*100
        vote_percent.append(z)
        
    winner_vote=max(vote_per_candidate)
    winner=unique_candidate[vote_per_candidate.index(winner_vote)]
    
    #index():The index() method returns the index of the element in the list.
        

print("Election Results")
print("-------------------------")
print("Total Votes: "+str(vote))
#print("-------------------------")

for i in range(len(unique_candidate)):
    print(unique_candidate[i]+": "+str(vote_percent[i])+"% ("
          +str(vote_per_candidate[i])+")")
print('-------------------------')
print("Winner: "+ winner)
print("-------------------------")


with open('Result2.txt', 'w') as text:

    text.write("Election Results\n")
    text.write("---------------------\n")
    text.write("Total Votes: "+str(vote)+"\n")
    text.write("---------------------\n")
    for i in range(len(unique_candidate)):
        text.write(unique_candidate[i]+": "+str(vote_percent[i])+"% ("
          +str(vote_per_candidate[i])+")\n")
    text.write("---------------------\n")
    text.write("Winner: "+winner+"\n")
    text.write("---------------------\n")   
        