dict1={}
num=int(input("Enter no. of students:"))
for i in range(num):
    n=input("Enter name:")
    c=int(input("Enter no. of competitions won:"))
    dict1[n]=c
print(dict1)
print(" ")
n=input("Enter name of student whose number of competitions is to be changed:")
c=int(input("Enter no. of competitions won:"))
dict1[n]=c
print("Updated dictionary:")
print(dict1)
    
