#include <stdio.h>
#include <cs50.h>

int main (int argc, string argv[])
{
    if (argc >= 2)
    {
        printf("hello, ");
        for (int i = 1; i < argc; i++)
        {
            printf("%s ", argv[i]);
        }
        printf("\n"); 
    }
    else
    {
        printf("no name found\n");
    }
}
