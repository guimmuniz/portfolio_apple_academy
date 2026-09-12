#include <stdio.h>
#include <cs50.h>

int fatorial(int n);

int main (void)
{
    int fac = get_int("De qual numero voce quer o fatorial? ");
    int result = fatorial(fac);
    printf("%i\n", result);
}

int fatorial(int n)
{
    if(n == 1)
    {
        return 1;
    }
    else
    {
    return n * fatorial(n-1);
    }
}
