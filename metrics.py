rows=int(input("Enter no. of rows:"))
col=int(input("Enter no. of columns:"))
l1=[]
k=0
l=range(rows*col)
for i in range(rows):
    for j in range(col):
        l[k]=input("Enter element:")
        k=k+1
        l1.append(k)

print(l1)


