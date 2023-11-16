#searching for an element in a list
list1=[]
num=int(input("Enter no. of elements: "))
for i in range(num):
    a=int(input("Enter element: "))
    list1.append(a)
print("Given list is",list1)
el=int(input("Enter an element to search in given list: "))
total=len(list1)
for i in range(0,total):
    if el==list1[i]:
        print(el,"is found in list at position",i)
        break
else:
    print(el,"is not present in the list.")
        
