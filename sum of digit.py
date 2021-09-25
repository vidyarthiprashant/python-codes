
i=int(input("enter number:"))
sum=0
while i>0:
    d=i%10
    sum=sum+d
    i=i//10
print("sum of digits:",sum)
