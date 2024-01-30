#Write a menu driven program to input names of n students,total mark,average, and result and store in
#nested tuple and display the following functions:
#1. Display name,mark,average and assign result as pass if average is more than or equal to 70
#and fail if average is less than 70
#2. Display name, total mark, and average of all students
#3. Accept name and display other details if found and not found if not exist
#4. Display students getting average mark more than or equal to 85

#Creating an empty tuple
tup=()

#Function to display those who have passed and failed
def func1():
    print(" ")
    for i in tup:
        print(i[0],"-",i[2])
        if i[2]>=70:
            print("Passed.")
        else:
            print("Failed.")

#Function to display all the details of the students in the tuple
def func2():
    print(" ")
    print("Details of all students are shown below.")
    for i in tup:
        print("Name:",i[0],"Total Marks:",i[1],"Average Marks:",i[2])

#Function to search for a name and check if they exist in the data or not
def func3():
    print(" ")
    na=input("Enter name to search:")
    for i in tup:
        if na in i:
            print(i)
            break
        else:
            print("Name does not exist.")
            break

#Function to display names of those who have average marks more than or equal to 85
def func4():
    print(" ")
    for i in tup:
        if i[2]>=85:
            print(i[0])
        else:
            pass

#The menu
print("============================NESTED TUPLE MENU============================")
print(" ")
print("Prepare the list.")
print(" ")

#Making the nested tuple with all the details
n=int(input("Enter number of students:" ))
for i in range(n):
    name=input("Enter name of student:" )
    total=int(input("Enter total mark:"))
    av=(total//3)
    print("Average marks:",av)
    tup += ((name,total,av),)

print("Data saved.")
print(" ")
print(" ")
#Displaying all the functions provided
print("Given below are different functions that you can choose to execute for the data.")
print("1.Display those who have passed and failed")
print("2.Display the info of all the students.")
print("3.Search for a name in the data and display their details.")
print("4.Display the names of students who have more than 85 average marks.")
print("========================================================")
print(" ")
print("Choose which function to run.")
while True:
    #Choosing a function
    opt=int(input("Enter choice ==> "))
    #Executes first function
    if opt==1:
        func1()
    #Executes second function
    if opt==2:
        func2()
    #Executes third function
    if opt==3:
        func3()
    #Executes fourth function
    if opt==4:
        func4()
    print(" ")
    print(" ")
    #Option to execute another function in the menu
    print("Would you like to execute another function? (Y/N)")
    opt2=input("==> ")
    #Goes back to line 79
    if opt2=="Y":
        continue
    #Exits the menu
    elif opt2=="N":
        print("==========Thank you for using the menu.==========")
        break
    

    

    
    
    
