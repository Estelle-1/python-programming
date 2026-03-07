#include<stdio.h>
void main()
{
int a,b,large;
printf("enter the two numbers: \n");
scanf("%d %d",&a,&b);
large=a>b?a:b;
printf("the smallest among the two numbers is %d",large);
}

