dict1={'brand':'suzuki','model':'dzire','year':2020}
dict2=dict1.copy()
print("Dic 2=",dict2)
x=('key1','key2','key3')
y=0
a=dict.fromkeys(x,y)
print(a)
x=dict2.setdefault("place","new delhi")
print(x)
dict2.update({"colour":"white"})
print(dict2)
