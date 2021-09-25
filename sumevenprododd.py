i=int(input("enter number ="))
sum=0
pro=1
while i>0:
    d=i%10
    if d%2==0:
        sum=sum+d
    else:
        pro=pro*d
    i=i//10
print("sum of even:",sum,"product of odd:",pro)
