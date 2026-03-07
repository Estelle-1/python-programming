#include<stdio.h>
#include<string.h>
void main()
{
  char s1[50],s2[50],nc;
  int choice,op1,op2;
  printf("First string: ");
  scanf("%s",s1);
  printf("Second string: ");
  scanf("%s",s2);
  printf("1. String Length \n");
  printf("2. String Copy \n");
  printf("3. String Concatenate \n");
  printf("4. String Comparison \n");
  while (1)
  {
    printf("Enter option:");
    scanf("%d",&choice);
    switch(choice)
    {
      case 1:
      printf("Length of first string: %zu \n",strlen(s1));         
      printf("Length of second string: %zu \n",strlen(s2));
      break;
      case 2:
      printf("Select destination string (1/2): ");
      scanf("%d",&op1);
      printf("Select source string (1/2): ");
      scanf("%d",&op2);
      if (op1==op2)
      {
          printf("Destination and source string cannot be the same! \n");
          break;
      }
      printf("Copied string \n");
      if(op1==1 && op2==2)
      {
          printf("%s \n",strcpy(s1,s2));
          break;
      } 
      else
      { 
          printf("%s \n",strcpy(s2,s1));
          break;
      }
      case 3:
      printf("Joined string: %s \n", strcat(s1,s2));
      break;
      case 4:
      if ((strcmp(s1,s2))==0)
      {
          printf("Both strings are equal \n");
          break;
      }
      else
      {
          printf("Both strings are not equal \n");
          break;
      }
    }
    printf("Do you want to execute another option: (y/n): ");
    scanf(" %c",&nc);
    if (nc=='y')
    {
        continue;
    }
    if (nc=='n')
    {
        printf("Exited program. \n");
        break;
    }
  }
}
