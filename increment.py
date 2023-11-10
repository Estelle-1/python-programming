#Write a program to increment the elements of a list with a number
list1= []
num=int(input("Enter limit:"))
for i in range(num):
    el=int(input("Enter element:"))
    list1.append(el)
print(list1)
print("")

n = int(input("Enter a number: "))
print("")

for i in range(len(list1)):
    list1[i] += n

print("List after increment:", list1) 
