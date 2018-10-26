#!/usr/bin/env python
# coding: utf-8

# In[ ]:


x=int(input ("Enter your number:"))
if x< -100:
    result= x*-1
elif x>=-100 and x<=-25:
    result=x**4
elif x> -25 and x<=0:
    result=(3*(x**2))-1
elif x>0 and x<= 100:
    result= ((22/7)/2)*x+3**x
else:
    result=x
        
print(result)
#D) Integers data, otherwise will results an errors.  
    



# In[ ]:




