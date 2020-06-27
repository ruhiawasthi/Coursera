#!/usr/bin/env python
# coding: utf-8

# In[1]:


largest = -1
smallest = None
while True:
   try: 
      num = input("Enter a number: ")
      if num == "done" :
          break
     
      n = int (num)
      if n>largest:
          largest = n
      if smallest is None or smallest > n:
          smallest = n
   except :
      print("Invalid input")  
        
print("Maximum is", largest)
print("Minimum is",smallest)

