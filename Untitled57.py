#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
total = 0
count = 0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:") : 
        total += float(line[line.find(":")+1:])
        count += 1        
    else: continue
        
print ("Average spam confidence:", total/count)

