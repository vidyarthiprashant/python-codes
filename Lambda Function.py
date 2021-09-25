
ages=[12,13,17,18,24,32]
b=filter(lambda a:a>18,ages)
c=list(map(lambda a:a*3,ages))
for x in c:
       print(x)
for x in b:
    print(x)
