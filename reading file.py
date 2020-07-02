#!/usr/bin/env python
# coding: utf-8

# In[1]:


fname = input("Enter file name: ")
fh = open(fname)
lst =list()
for line in fh:
    word= line.rstrip().split()    # to eliminate the unwanted blanks and turn the line into a list of words
    for element in word:           # check every element in word    
        if element in lst:         # if element is repeated
            continue               # do nothing
        else :                     # else if element is not in the list
            lst.append(element)    # append     
lst.sort()                         # sort the list (de-indent indicates that you sort when the loop ends)
print (lst)          

