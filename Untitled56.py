#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
for i in fh:
    i = i.rstrip().upper()
    print(i)

