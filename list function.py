a=[]
s=int(input("enter size"))
for i in range(s):
    x=input("enter values")
    a.append(x)
    print(a)
x=input("enter item to know the freq")
f=a.count(x)
print("freq",f)
d=a.index(i)
print(d)
