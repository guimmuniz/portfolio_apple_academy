#include <stdio.h>
#include <cs50.h>

int collatz (int c);

int main (void)
{
    int n = get_int("Digite um numero: ");
    int result = collatz(n);
    printf("%i\n", result);
}

int collatz (int c)
{
    if(c==1)
    {
        return 0;
    }
    else if((c%2)==0)
    {
        return 1 + collatz(c/2);
    }
    else
    {
        return 1 + collatz(3*c+1);
    }
}
