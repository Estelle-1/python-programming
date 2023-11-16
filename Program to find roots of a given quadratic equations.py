import math
a=int(input("enter the first num"))
b=int(input("enter the second num"))
c=int(input("enter the third num"))
d=b*b-4*a*c
if d>0:
    r1=(-b)+math.sqrt(d)/2*a
    r2=(-b)-math.sqrt(d)/2*a
    print(r1,r2)
else:
    print("no root")
    
    
