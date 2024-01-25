#Create a nested tuple that has marks of at least 5 students obtained in 3 subjects. Now, perform
#the following operations on it.
#a.Display the marks of the fourth student
#b.Display the marks obtained by the second student in the first subject.
#c.Display the total marks obtained by each student
#d.Find the average marks obtained by each student
#e.Using the average marks obtained by each student, calculate the average marks obtained by all students
#f.For each student display the maximum and minumum marks obtained

t1=()
n=int(input("Enter number of students:"))
for i in range(n):
    print("Enter marks of student", i+1)
    m1=int(input("Enter marks for first subject:"))
    m2=int(input("Enter marks for second subject:"))
    m3=int(input("Enter marks for third subject:"))
    t1= t1 + ((m1,m2,m3),)
    print(" ")

print(t1)
print(" ")
print("Marks of fourth student:", t1[3])
print(" ")
print("Marks obtained in first subject by second student:", t1[1][0])
print(" ")
a=sum(t1[0])
b=sum(t1[1])
c=sum(t1[2])
d=sum(t1[3])
e=sum(t1[4])
print("Total marks obtained by each student:")
print("1.",a)
print("2,",b)
print("3.",c)
print("4.",d)
print("5.",e)
print(" ")
l1=len(t1[0])
l2=len(t1[1])
l3=len(t1[2])
l4=len(t1[3])
l5=len(t1[4])
print("Average marks obtained by each student:")
print("1.",a/l1)
print("2,",b/l2)
print("3.",c/l3)
print("4.",d/l4)
print("5.",e/l5)
print(" ")
ltotal=l1+l2+l3+l4+l5
print("Average marks obtained by all students:")
print(ltotal/5)
print(" ")
max1=max(t1[0])
max2=max(t1[1])
max3=max(t1[2])
max4=max(t1[3])
max5=max(t1[4])
min1=min(t1[0])
min2=min(t1[1])
min3=min(t1[2])
min4=min(t1[3])
min5=min(t1[4])
print("Maximum and minimum marks for each student:")
print("1. Maximum:",max1," Minumum:",min1)
print("2. Maximum:",max2," Minumum:",min2)
print("3. Maximum:",max3," Minumum:",min3)
print("4. Maximum:",max4," Minumum:",min4)
print("5. Maximum:",max5," Minumum:",min5)



    
