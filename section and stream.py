#write a program to input total number of sections and streams in class 11 and display all information on the output screen

list1={}
section=int(input("Enter number of sections:"))
for i in range(section):
    a=input("Enter section:")
    b=input("Enter stream:")
    list1[a]=b
print(list1)

