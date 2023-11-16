#Program to find sum of n natural numbers
n=int(input("Enter number of natural numbers: "))
sum=0
a=0
if n<0:
    print("Enter a positive value!")
else:
    while (a<=n):
        sum+=a
        a=a+1
    print("Sum of",n,"natural numbers is",sum)  


    
    
