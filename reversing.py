list1=[]
num=int(input("Enter limit:"))
for i in range(num):
    el=int(input("Enter element:"))
    list1.append(el)
print(list1)
print("")
n=list1.sort(reverse=True)
print("Reversed:",list1)
