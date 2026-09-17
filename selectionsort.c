//Write a C program to sort an array using selection sort
#include<stdio.h>
void main()
{
  int n,i,j,pos,small,temp;
  printf("Enter number of elements:");
  scanf("%d",&n);
  int a[n];
  printf("Enter elements \n");
  for(i=0;i<n;i++)
  {
    scanf("%d",&a[i]);
  }
  printf("Current Array: ");
  for(i=0;i<n;i++)
  {
    printf("%d ",a[i]);
  }
  printf("\n");
  for(i=0;i<n-1;i++)
  {
    small=a[i];
    pos=i;
    for(j=i+1;j<n;j++)
    {
      if(small>a[j])
      {
        small=a[j];
        pos=j;
      }
    }
    if(pos!=i)
    {
      temp=a[i];
      a[i]=a[pos];
      a[pos]=temp;
    }
  }
  printf("After Selection Sort: ");
  for(i=0;i<n;i++)
  {
    printf("%d ",a[i]);
  }
  printf("\n");
}
