#create a dictionary with employer no. as key and employer name as values. write a program to
#input an employer number and delete it from the dictionary. display an error message that says employer does not exist



dict1={}
num=int(input("Enter number of employers:"))
for i in range(num):
    number=int(input("Enter employer number:"))
    name=input("Enter employer name:")
    dict1[number]=name
print(dict1)

a=int(input("Enter employee number to remove from the dictionary:"))

if a<=num:
    dict1.popitem()
    print("Updated dictionary:")
    print(dict1)

else:
    print('UNKNOWN_EMPLOYEE_ERROR : Employee does not exist in dictionary.')



