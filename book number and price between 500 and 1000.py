#Write a dictionary Book of format Book number and price and display the total
#number of books whose price is in between 500 and 1000

Book={}
Price=[]
num=int(input("Enter number of books:"))
for i in range(num):
    n=int(input("Enter book number:"))
    p=int(input("Enter book price:"))
    Book[n]=p
    if p>500 and p<1000:
        Price.append(p)
print(" ")
print(Book)
print(" ")
print("Number of books whose price is between 500 and 1000 are given below:")
print(" ")
print(len(Price))






