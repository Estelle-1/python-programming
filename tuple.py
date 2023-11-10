list1=[]
t=()
num=int(input("Enter limit: "))
for i in range(num):
    s=int(input("Enter element:"))
    list1.append(s)
t=tuple(list1)
print(t)
