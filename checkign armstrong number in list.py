#write a program to input a list and test if a number is equal to the sum of the cube of 
#its digits and find the smallest and largest such number from the list
list1=eval(input("Enter a list: "))
a=[]
b=len(list1)
for i in range(b):
    num=list1[i]
    los=0
    while num:
        digit=num%10
        los+=digit*digit*digit
        num=num//10
    if los==list1[i]:
        a.append(list1[i])

print("Largest number equal to the sum of cube of its digits is", max(a))
print("Smallest number equal to the sum of cube of its digits is", min(a))
        
        

    

