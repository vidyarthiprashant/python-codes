
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
print(count)
