//C program to calculate factorial using recursion.
#include<stdio.h>
int i=1,num,f=1,fact;
int factorial(int n)
{
    while(i<=n)
    {
        f*=i;
        i++;
        factorial(n);
    }
    return f;
}
void main()
{
    printf("Enter a number: ");
    scanf("%d",&num);
    fact=factorial(num);
    printf("The factorial of %d is %d \n.",num,fact);
}
