//Program to display a string in both lowercase and uppercase 
#include<stdio.h>
int i;
void lower(char s[])
{
    i=0;
    while(s[i]!='\0')
    {
      if (s[i]>='A' && s[i]<='Z')
      {
          s[i]=s[i]+32;
          i++;
      }
      else
      {
          i++;
      }
    }
    printf("The given string in lowercase is %s \n.",s);
}
void upper(char s[])
{
    i=0;
    while(s[i]!='\0')
    {
      if (s[i]>='a' && s[i]<='z')
      {
          s[i]=s[i]-32;
          i++;
      }
      else
      {
          i++;
      }
    }
    printf("The given string in uppercase is %s \n.",s);
}
void main()
{
    char string[50];
    printf("Enter a string: ");
    scanf("%s",string);
    upper(string);
    lower(string);
}
