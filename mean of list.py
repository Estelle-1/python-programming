#calculating mean of a given list of numbers
list1=[]
num=int(input("Enter no. of elements: "))
for i in range(num):
    a=int(input("Enter element: "))
    list1.append(a)
print(list1)
div=len(list1)
b=sum(list1)
mean=b//div
print("Mean of given list of numbers is",mean)
