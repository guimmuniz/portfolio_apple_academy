#include <stdio.h>
#include <cs50.h>

void draw(int layer);

int main (void)
{
    int num = get_int("Quantas camadas de piramide voce quer? ");
    draw(num);
}

void draw(int layer)
{
    for (int i = 1; i <= layer; i++)
    {
        for (int j = 0; j < i; j++)
        {
            printf("#");
        }
        printf("\n");
    }
}
