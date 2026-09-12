#include <stdio.h>
#include <cs50.h>

bool realtriangle (float a, float b, float c);

int main (void)
{
    float x = get_float("Give me the first side of a triangle: ");
    float y = get_float("Give me the second side of a triangle: ");
    float z = get_float("Give me the third side of a triangle: ");
    bool TrueFalse = realtriangle(x,y,z);
    if (TrueFalse == 1)
    {
        printf("The triangle can exist!\n ");
    }
    else
    {
        printf("The triangle can't exist!\n");
    }
}

bool realtriangle (float a, float b, float c)
{
    if (a > 0 && b > 0 && c > 0)
    {
        if ((a+b) > c && (a+c) > b && (b+c) > a)
        {
            return 1;
        }
        else
        {
            return 0;
        }
    }
    else
    {
        return 0;
    }
}
