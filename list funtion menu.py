#Menu-driven program for different functions of list

list1=[]
list2=[]

#Main Menu
print("=====================LIST FUNCTION MENU=====================")
print(" ")
m=int(input("Enter number of values you want to enter to initial list: "))
for i in range(m):
    n=int(input("Enter element: "))
    list1.append(n)
print("The given list is:")
print(list1)

print()
print("Given below are functions for a list.")
print()
print("1.Appending a list")
print("2.Inserting an element to a list")
print("3.Appending another list to given list")
print("4.Modifying an element in given list")
print("5.Deleting an existing element from position in given list")
print("6.Deleting an existing element with given value")
print("7.Sorting the list in accending order")
print("8.Sorting the list in decending order")
print("9.Displaying the given list")
print()
print("Which function would you like to run?")
print(" ")
print("============================================================")
while True:
    #Choosing function
    option=int(input("Option:"))
    #Appending an element to initial list
    if option==1:
        print(list1)
        a=int(input("Enter the value that you want to add to the list: "))
        list1.append(a)
        print(list1)
    
    #Inserting an element to a position in initial list
    elif option==2:
        print(list1)
        a=int(input("Enter the value that you want to add to the list: "))
        b=int(input("Enter the position that you want to put the value in the list: "))
        list1.insert(b,a)
        print(list1)

    #Appending another list to initial list
    elif option==3:
        print(list1)
        n=int(input("How many elements do you want to enter for the second list: "))
        for i in range(n):
            e=int(input("Enter the elements: "))
            list2.append(e)
        print("The second list is given below")
        print(list2)
        print()
        print("Appending second list to first list.")
        list1.append(list2)
        print(list1)

    #Modifying a selected element in initial list
    elif option==4:
        print(list1)
        c=len(list1)
        a=int(input("Enter the position of the element that you want to modify: "))
        if a<c:
            print("Element of given position is:",list1[a])
            b=int(input("Enter new element to modify old element: "))
            list1[a]=b
            print(list1)
        else:
            print("Position of out of range.")

    #Deleting an existing element from initial list with a given position
    elif option==5:
        print(list1)
        a=int(input("Enter position of element that you want to remove: "))
        list1.remove(list1[a])
        print(list1)

    #Deleting an existing element from initial list with a given value
    elif option==6:
        print(list1)
        a=int(input("Enter the element that you want to remove from the list: "))
        list1.remove(a)
        print(list1)

    #Sorting initial list in accending order
    elif option==7:
        print(list1)
        print("Sorting the list in accending order")
        list1.sort()
        print(list1)

    #Sorting initial list in decending order
    elif option==8:
        print(list1)
        print("Sorting the list in decending order")
        list1.sort(reverse=True)
        print(list1)

    #Displaying initial list
    elif option==9:
        print("Displaying given list.")
        print(list1)

    #Choosing another function to execute
    print("Would you like to execute another function?")
    print("1.Yes")
    print("2.No")
    option2=int(input("="))
    if option2==1:
        #Goes back to previous program to select another function
        continue
    #Stops the program
    elif option2==2:
        print("=====Thank you for using the menu.=====")
        break


