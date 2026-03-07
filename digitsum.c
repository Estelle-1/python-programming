//Program to find the sum of the digits of a number using function
#include<stdio.h>
int dsum(int n)
{
  int temp,sum,digit;
  temp=n;
  while (temp>0)
  {
    digit=temp%10;
    sum+=digit;
    temp/=10;
  }
  return sum;
}
void main()
{
  int a,s;
  printf("Enter a number:");
  scanf("%d",&a);
  s=dsum(a);
  printf("The sum of the digits of %d is %d. \n",a,s);
}
