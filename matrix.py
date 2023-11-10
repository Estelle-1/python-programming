r=int(input("Enter no. of rows:"))
c=int(input("Enter no. of columns:"))
matrix = []

for i in range(r):
   
   row = []
   for j in range(c):
      
      element = int(input("Enter element:"))
      
      row.append(element)
      
   matrix.append(row)

print(matrix,end=' ')
print()
