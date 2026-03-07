//C program to find the largest among a set of numbers using command line argument
#include<stdio.h>
#include<stdlib.h>
void main(int argc, char *argv[])
{
    int i,largest;
    largest=atoi(argv[1]);
    for(i=1;i<argc;i++)
    {
        if (atoi(argv[i])>largest)
        {
            largest=atoi(argv[i]);
        }
    }
    printf("Largest number among the given numbers is %d \n.",largest);
} 
