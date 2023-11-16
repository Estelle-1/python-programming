#program to find frequencies of all elements of a list
#and print the unique elements in a new list and duplicate element in another list

list1=eval(input("Enter a list:"))
n=len(list1)
listunique=[]
listduplicate=[]
count=i=0
while i<n:
    el=list1[i]
    count=1
    if el not in listduplicate and el not in listunique:
        i+=1
        for j in range(i,n):
            if el==list1[j]:
                count+=1

        else:
            print("Frequency of",el,"in list:",count)
            if count==1:
                listunique.append(el)
            else:
                listduplicate.append(el)
    else:
        i+=1

print("Initial list:","[",list1,"]")
print("List containing duplicates of elements in initial list",listduplicate)
print("List containing unique elements in initial list",listunique)
