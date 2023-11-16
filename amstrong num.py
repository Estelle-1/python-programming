num=int(input("enter the number"))
sum=0
n=len(str(num))
temp=num
while temp>0:
    digit=temp%10
    sum+=digit*2n
    temp//=10
if num==sum:
    print("it is a amstrong num")
else:
    print("its is not an amstrong num")
    
