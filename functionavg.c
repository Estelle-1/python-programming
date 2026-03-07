#include<stdio.h>
void avg (void)
{
    float a,n,i,num,sum=0;
    printf("Enter the number of elements:");
    scanf("%f",&n);
    printf("Enter elements:\n");
    for(i=0;i<n;i++)
    {
        scanf("%f",&num);
        sum=sum+num;
    }
    a=sum/n;
    printf("The average of the given number is %f. \n",a);
}
void main()
{
avg();
}

