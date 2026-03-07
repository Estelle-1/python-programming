#include<stdio.h>
void main()
{
  int e,n,a[50],i,j;
  printf("Enter number of elements:");
  scanf("%d",&n);
  printf("Enter elements \n");
  for(i=0;i<n;i++)
  {
    scanf("%d",&a[i]);
  }
  printf("Current Array \n");
  for(i=0;i<n;i++)
  {
    printf("%d \t",a[i]);
  }
  printf("\n");
  //Sorting array
  for(i=0;i<n;i++)
  {
    for(j=i+1;j<n;j++)
    {
      if(a[i]>a[j])
      {
        e=a[i];
        a[i]=a[j];
        a[j]=e;
      }
    }
  }
  printf("Array sorted in ascending order \n");
  for(i=0;i<n;i++)
  {
    printf("%d \t",a[i]);
  }
  printf("\n");
}
