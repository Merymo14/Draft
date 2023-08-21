#!/usr/bin/env python
# coding: utf-8

# In[72]:


import csv
import os



file_to_load = os.path.join(".", "pypoll","Resources", "election_data.csv")

file_to_output = os.path.join(".", "election_analysis.txt")

#1
total_votes = 0

#2
candidate_votes = {}
candidate_options = []


#3
Winning_candidate = ""
Winning_count = 0


with open(file_to_load) as election_data:
    reader = csv.reader(election_data)
    
    header = next(reader)
    print(header)
    
    
    for row in reader:
        
        total_votes = total_votes + 1
        #print(row)
        
        candidate_name = row[2]
        
     
        if candidate_name not in candidate_options:
            
            candidate_options.append(candidate_name)
            
            candidate_votes[candidate_name] = 0
            
        candidate_votes[candidate_name] += 1
            
            
print(candidate_votes)           
print(candidate_options)
    

with open(file_to_output, "w") as txt_file:      
    election_results = (
        f"Election Results\n"
        f"-----------------------\n"
        f"Total Votes {total_votes}\n"
        f"-----------------------\n"
    )     
    print(election_results, end="")
    
    txt_file.write(election_results)
    
    
    for candidate in candidate_votes:
        
        votes = candidate_votes[candidate]
        vote_percentage = float(votes) / float(total_votes) * 100
      
      
  
    
            
        voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
       
         
        print(votes)
        print(vote_percentage)
        
        print(voter_output, end="")
        
        txt_file.write(voter_output)
        
    
            
    print("Winner:Diana DeGette")
    
        
    
        


# In[ ]:





# In[ ]:




