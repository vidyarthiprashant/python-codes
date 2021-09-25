
i=int(input("enter number:"))
sum=0
arm=i
while i>0:
    d=i%10
    sum=sum+d*d*d
    i=i//10
if arm==sum:
    print("No is Armstrong:",sum)
else:
    print("No is not Armstrong")
