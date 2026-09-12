#include <stdio.h>
#include <cs50.h>

void meow(int n);
int get_positive(void);

int main(void)
{
    int times = get_positive();
    meow(times);
}

int get_positive(void)
{
    int n;
    do
    {
        n = get_int("How many times do you want the cat meow? ");
    }
    while (n < 1);
    return n;
}

void meow(int n)
{
    for (int i = 0; i < n; i++)
    {
        printf("meow\n");
    }
}
