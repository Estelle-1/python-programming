#include<stdio.h>
void main()
{
  int i,n,search,count=0;
  printf("Enter number of elements: ");
  scanf("%d",&n);
  int a[n];
  printf("Enter elements\n");
  for(i=0;i<n;i++)
  {
    scanf("%d",&a[i]);
  }
  printf("Enter search element: ");
  scanf("%d",&search);
  for(i=0;i<n;i++)
  {
    if(a[i]==search)
    {
      printf("Element found at index %d.\n",i);
      count=1;
      break;
    }
  }
  if(count==0)
  {
    printf("Element not found!\n");
  }
}
