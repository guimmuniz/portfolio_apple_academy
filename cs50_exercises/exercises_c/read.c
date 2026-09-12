#include <stdio.h>

int main (int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Give a file!");
    }
    char *file = argv[1];
    FILE *input = fopen(file, "r");
    char ch;
    while((ch = fgetc(input)) != EOF)
    {
        printf("%c", ch);
    }
}
