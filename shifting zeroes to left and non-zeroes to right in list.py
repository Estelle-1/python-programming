#Program to input a list of numbers and shift all zeros to right and all non-zero numbers to left of the list

list1=[]
num=int(input("Enter limit:"))
for i in range(num):
    el=int(input("Enter element:"))
    list1.append(el)
print(list1)
print("")
n=len(list1)
end=n-1
i=0
while i<=end:
    el=list1[i]
    if el==0:
        for j in range(i,end):
            list1[j]=list1[j+1]
        else:
            list1[end]=0
            end-=1
    if list1[i]!=0:
        i+=1
print(list1)
