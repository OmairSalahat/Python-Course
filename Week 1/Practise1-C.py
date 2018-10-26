#!/usr/bin/env python
# coding: utf-8

# In[ ]:


x=float(input("Enter the tempreture"))
y=int(input("If the temp. in Fahrenheit Enter 1, if the temp. in Celsius Enter 2"))
if y==1:
    x=x-17.2222222
    print(f"{x} , Celsius")
elif y==2:
    x=x+17.2222222
    print(f"{x} , Fahrenheit")   


# In[ ]:




