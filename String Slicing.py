#!/usr/bin/env python
# coding: utf-8

# In[5]:


text = "X-DSPAM-Confidence:    0.8475";
ntext = text.find('0')

ztext=text[ntext:]

ztext=float(ztext)

print(ztext)

