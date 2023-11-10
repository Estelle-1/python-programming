l1=[]
l2=[]
num=int(input("Enter limit for both tuples: "))
for i in range (num):
    e1=int(input("Enter element for first tuple:"))
    l1.append(e1)
    e2=int(input("Enter element for second tuple:"))
    l2.append(e2)
t1=tuple(l1)
t2=tuple(l2)
print("First tuple:",t1)
print("Second tuple:",t2)
print(" ")
print("Swapping values of both tuples")
t1,t2=t2,t1
print("Swapped values of first tuple:",t1)
print("Swapped values of second tuple:",t2)
