#!/usr/bin/env python
# coding: utf-8

# In[17]:


import numpy as ch
a=[]
s=int(input("enter size : "))
for i in range(s):
    v=int(input("enter values : "))
    a.append(v)
ar=ch.array(a)
for i in range(ar.size):
    print(ar[i])
d=ar[-2:]
print(d)


#  

# In[29]:


ar=ch.random.randint(1,50,10)
print(ar)
print(ar.shape)
ar=ar.reshape(5,2)
print(ar)
ar=ar.reshape(10)
print(ar)
print(ar.ndim)
print(ar.shape)


# In[31]:


ch.random.seed(12)
ar =  ch.random.randint(1,100,12)
print(ar)
   


# In[ ]:


matrix=[]
import numpy as np
row=int(input('Enter the number of rows:'))
col=int(input('Enter the number of columns:'))

for i in range(row):
    a=[]
    for j in range(col):
        val=int(input('Enter the numbers: '))
        a.append(val)
    print(a)
    matrix.append(a)
print(matrix)
arr=np.array(matrix)
arr


# In[ ]:


a=[]
s=int(input("enter size of list : "))
for i in range(s):
    v=int(input("enter value : "))
    a.append(v)
e=0
o=0
for i in range(s):
    if a[i]%2==0:
        e=e+1
        else:
            o=o+1
print("total even" : ",e,"total odd",o)


# In[ ]:


a=[]
s=int(input("enter size of list : "))
for i in range(s):
    v=int(input("enter value : "))
    a.append(v)
e=0
o=0
for i in range(s):
    if a[i]%2==0:
        e=e+1
    else:
        o=o+1
print("total even",e,"total odd",o)


# In[11]:


a=[]
s=int(input("enter size"))
for i in range(s):
    v=int(input("enter value"))
    a.append(v)
b=int(input("no to search"))
c=0
for i in range(s):
    if a[i]==b:
        c=1
        p=i+1
        break
if(c==1):
    print("element found at",p,"position")
else:
    print("not found")


# In[ ]:


import numpy as ch
a=[]
s=int(input("enter size."))
for i in range(s):
    v=int(input("enter values-"))
    a.append(v)
f=int(input("enter no whose freq u want"))
count=0
for i in range(s):
    if a[i]==f:
        count=count+1
    print(f)


# In[56]:


matrix=[]
import numpy as np
row=int(input('Enter the number of rows:'))
col=int(input('Enter the number of columns:'))

for i in range(row):
    a=[]
    for j in range(col):
        val=int(input('Enter the numbers: '))
        a.append(val)
    print(a)
    matrix.append(a)
print(matrix)
arr=np.array(matrix)
print(arr)


# In[ ]:




