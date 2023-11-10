#Write a program that reverses the list of integers (in place).

list1=[]
num=int(input("Enter limit:"))
for i in range(num):
    el=int(input("Enter element:"))
    list1.append(el)
print("")
print(list1)
print("Reversed:")
n=list1.sort(reverse=True)
print(list1)
