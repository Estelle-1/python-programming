#Program to input two lists and create a third that contains all elements of the first followed by all the elements in the second

l1=[]
l2=[]
l3=[]
num=int(input("Enter limit:"))
for i in range(num):
    e1=int(input("Element for 1st:"))
    l1.append(e1)
    e2=int(input("Element for 2nd:"))
    l2.append(e2)
print(l1)
print(l2)
l3=l1+l2
print("Third list:",l3)
