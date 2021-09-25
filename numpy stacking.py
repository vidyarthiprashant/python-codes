#!/usr/bin/env python
# coding: utf-8

# In[23]:


import numpy as c
c.random.seed(122)
a1=c.random.randint(1,21,9).reshape(3,3)
a2=c.random.randint(31,51,9).reshape(3,3)
print(a1)
print(a2)
print(c.hstack((a1,a2)))
print(c.vstack((a1,a2)))


# In[ ]:





# In[ ]:




