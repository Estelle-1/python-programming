#Write a python statement for each of the following tasks using built-in functions only
#1.To remove the element 5 from list L
#2.To remove the last element from the list L

print("Given below is a list L.")
print(" ")
L=[1,2,3,4,5,6,7,8,9,10]
print(L)
print(" ")
#Removing element 5 from list L
a=int(input("Enter element to be removed from list:"))
b=(L.remove(a))
print(L)
print(" ")
#Removing the last element from list L
print("Removing last element from the list...")
c=(L.pop(-1))
print(L)

