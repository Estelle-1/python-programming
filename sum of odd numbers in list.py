#given a list of integers, write a program to find the sum of odd elements in the list

list1=[]
num=int(input("Enter number of elements to be inputted in the list: "))
for i in range(num):
    a=int(input("Enter element:"))
    list1.append(a)
print("Given list of integers is",list1)
b=0
sum=0
while b<len(list1):
    if list1[b]%2==1:
        print(list1[b],"is odd.")
        sum=sum+list1[b]
    b=b+1
print("Sum of all odd integers in given list is",sum)
