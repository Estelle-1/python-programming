//Bubble Sort
#include<stdio.h>
void main()
{
  int n,i,j,max;
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
  for(i=0;i<n;i++)
  {
    for(j=0;j<n-i-1;j++)
    {
      if(a[j]>a[j+1])
      {
        max=a[j];
        a[j]=a[j+1];
        a[j+1]=max;
      }
    }
  }
  printf("After Bubble Sort: ");
  for(i=0;i<n;i++)
  {
    printf("%d ",a[i]);
  }
  printf("\n");
}
