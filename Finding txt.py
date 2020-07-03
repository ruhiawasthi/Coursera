#!/usr/bin/env python
# coding: utf-8

# In[15]:


name = input("Enter file:")
if len(name) < 1 : name = "finding.txt"
handle = open(name)

#words = text.split()

words = list()
counts = dict()
for line in handle:
    if line.startswith("From:") : 
        
        words = line.split()
        counts[words[1]] = counts.get(words[1], 0) +1 

print(words)     
maxval = None
maxkey = None
for key,val in counts.items() :
    if maxval == None or val>maxval:
      maxval = val
      maxkey = key   

print (maxkey, maxval)

