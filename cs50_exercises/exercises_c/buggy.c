#include <stdio.h>
#include <cs50.h>

void print_collumn(int height);

int main (void)
{
        int h = get_int("Height: ");
        print_collumn(h);
}

void print_collumn(int height)
{
    for (int i = 0; i < height; i++)
    {
        printf("#\n");
    }
}
