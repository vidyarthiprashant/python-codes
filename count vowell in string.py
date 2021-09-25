a=input("enter string")
vowel=0
con=0
for i in range(0,len(a)):
    a[i]!=" "
    if(a[i]=="a" or a[i]=="e" or a[i]=="i" or a[i]=="o" or a[i]=="u"):
        vowel=vowel+1
    else:
        con=con+1
        
print("vowel=",vowel)
print("consonant=",con)
