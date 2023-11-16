#to find the lowest and second lowest integer from 10 integers
small=smaller=0
for i in range(5):
    n=int(input("enter the number:"))
    if i==0:                        #first number read
        small=n
    elif i==1:                      #second number read
        if n<=small:
           smaller=n
        else: 
            smaller=small
            small=n
    else:                               #for every integer read 3rd integer onwards
        if n<smaller:
           small=smaller
           smaller=n
        elif n<small:
           small=n
print("The LOWEST NUMBER IS:",smaller)
print("THE SECOND LOWEST NUMBER IS:",small)
