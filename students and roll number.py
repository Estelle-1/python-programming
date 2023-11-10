dict1={}
num=int(input("Enter number of students: "))
for i in range (num):
    rollno=int(input("Enter roll no:"))
    marks=int(input("Enter marks:"))
    dict1[rollno]=marks
print(dict1)

choice='Yes'
while choice=='Yes':
    print("Enter details of new student.")
    rollno=int(input("Enter roll no. of new student:"))
    marks=int(input("Enter marks of new student:"))
    dict1[rollno]=marks
    choice=input("Do you want to add details of another student? (Yes/No):")
print("Dictionary after adding the details of new students:")
print(dict1)

