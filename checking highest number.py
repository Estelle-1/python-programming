#Program to display which of three given numbers by user is greatest

a=int(input("Enter first number:"))
b=int(input("Enter the second no:"))
c=int(input("Enter the third number"))
if (a>b) and (a<c):
    print(a," is greater")
if (b>c) and (b>a):
    print(b," is greater")
if (c>b) and (c>a):
    print(c," greater")

    

    
