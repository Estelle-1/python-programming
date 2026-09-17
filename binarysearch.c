#include<stdio.h>
void main()
{
  int i,j,n,mid,search,max,count;
  printf("Enter number of elements: ");
  scanf("%d",&n);
  int a[n],beg=0,end=n-1;
  printf("Enter elements\n");
  for(i=0;i<n;i++)
  {
    scanf("%d",&a[i]);
  }
  printf("Sorting Array for Binary Search...\n");
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
  printf("Enter search element: ");
  scanf("%d",&search);
  while(beg<end)
  {
    mid=(beg+end)/2;
    if(a[mid]==search)
    {
      printf("Element found at index %d.\n",mid);
      count=1;
      break;
    }
    else if(a[mid]>search)
    {
      end=mid-1;
      continue;
    }
    else if(a[mid]<search)
    {
      beg=mid+1;
      continue;
    }
  }
  if(count==0)
  {
    printf("Element not found!\n");
  }
}
