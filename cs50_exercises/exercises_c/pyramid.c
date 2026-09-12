#include <stdio.h>
#include <cs50.h>

void print_row(int bricks, int total);

int main (void)
{
    int layers;
    do
    {
        layers = get_int("How many layers do you want the pyramid have? ");
    }
    while (layers < 1);
    for (int i = 1; i <= layers; i++)
    {
        print_row(i, layers);
    }
}

void print_row(int bricks, int total)
{
    for (int i = 0; i < total - bricks; i++)
    {
        printf(" ");
    }
    for (int i = 0; i < bricks; i++)
    {
        printf("#");
    }
    printf("\n");
}
