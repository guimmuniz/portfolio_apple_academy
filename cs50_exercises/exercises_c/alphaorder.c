#include <stdio.h>
#include <cs50.h>
#include <string.h>

int main (void)
{
    string word = get_string("Type one word in lowercase: ");
    int counter = 0;
    for (int i = 0; i < strlen(word); i++)
    {
        if (word[i] > word[i-1])
        {
            counter = counter + 1;
        }
    }
    if (counter == strlen(word))
    {
        printf("It's in alphabetical order!\n");
    }
    else
    {
        printf("It isn't in alphabetical order!\n");
    }
}

