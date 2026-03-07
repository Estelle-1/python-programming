#include<stdio.h>
void main()
{
int days,months,rdays;
printf("enter number of days:");
scanf("%d",&days);
months=days/30;
rdays=days%30;
printf("no.of months=%d \n",months);
printf("no.of remaining days=%d \n",rdays);
}



