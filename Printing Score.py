#!/usr/bin/env python
# coding: utf-8

# In[2]:


ip = input("Enter Score: ")


score= float(ip)
if(score >= 1.0):
    print("you didn't follow instructions")
    exit()
elif(score >=0.9):
     print("A")
elif(score >= 0.8):
     print("B")
elif(score >= 0.7):
     print("C")
elif(score >= 0.6):
     print("D")
else:
     print("F")
        
        

