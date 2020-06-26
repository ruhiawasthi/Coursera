#!/usr/bin/env python
# coding: utf-8

# In[1]:



def computepay(h,r):
    if h<= 40:
           return h*r
    else:
           return (40*r)+(h-40)*1.5*r
    
hrs = input('Enter Hours:')
hr = float(hrs)
rate = input('Enter rate:')
rt = float(rate)

pay = computepay(hr,rt)
print("Pay" ,pay)

