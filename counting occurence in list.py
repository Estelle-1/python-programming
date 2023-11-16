#To count occurence of given element in a list
list1=[]
num=int(input("Enter no. of elements: "))
for i in range(num):
    a=int(input("Enter element: "))
    list1.append(a)
print("Given list is",list1)
el=int(input("Enter an element to count occurence: "))
total=len(list1)
for i in range(0,total):
    if el==list1[i]:
        print(el,"is found in list.")
        b=list1.count(el)
        print(el,"occurs in list",b,"times.")
        break
else:
    (el,"is not present in the list.")
    
