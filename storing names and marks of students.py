#create a dictionary which store marks of students with roll no. as key and the
#mark as value. get no. of students as input

dict1={}
stuno=int(input("Enter number of students:"))
for i in range(stuno):
    rollnoandname=input("Enter roll number and name of student:")
    mark=int(input("Enter mark of student:"))
    dict1[rollnoandname]=mark
print(dict1)
