import json

dict1={}
num=int(input("Enter number of elements:"))
for i in range (num):
    key=int(input("Enter number:"))
    value=input("Enter value:")
    dict1[key]=value
print (dict)
print(" ")
print(json.dumps(dict1, indent=2))
