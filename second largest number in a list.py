#Program to find the second largest number of a list of numbers

list1=[]
num=int(input("Enter limit:"))
for i in range(num):
    el=int(input("Enter element:"))
    list1.append(el)
print(list1)
n=len(list1)
b=sb=list1[0]
for i in range(1,n):
    if list1[i]>b:
        sb=b
        b=list1[i]
    elif list1[i]>sb:
        sb=list[i]
print("Largest number:",b)
print("")
print("Second largest number:",sb)
