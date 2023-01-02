#!/usr/bin/env python
# coding: utf-8

# # Write a Python program to reverse a string.
# 

# In[2]:


x=str(input('enter the word to be reversed:'))
l=len(x)
for i in range(l-1,-1,-1):
    print(x[i],end="")



