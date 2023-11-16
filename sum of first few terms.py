print("Enter values to find sum of the following pattern:")
print("1+x+x^2+x^3+x^4+....x^n")
x=float(input("Enter coefficient: "))
n=int(input("Enter number of terms: "))
num=0
for i in range(n+1):
    num+=x**i
print("Sum of the first",n,"is =",num)
