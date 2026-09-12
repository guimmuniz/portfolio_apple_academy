#include <cs50.h>
#include <stdio.h>

int main (void)
{
    int array[5];
    array[0] = 1;
    for (int i = 1; i < 5; i++)
        {
            array[i] = array[i - 1] * 2;
        }
    for (int i = 0; i < 5; i++)
        {
            printf("%d\n", array[i]);
        }
}
