#include <cs50.h>
#include <stdint.h>
#include <stdio.h>

int main (int argc, string argv[])
{
    if (argc != 2)
    {
        printf("Give a PDF File!\n");
        return 1;
    }
    string file = argv[1];
    FILE *input = fopen(file, "r");

    uint8_t buffer[4];

    uint8_t signature[] = {0x25, 0x50, 0x44, 0x46};

    fread(buffer, sizeof(uint8_t), 4, input);

    for (int i=0; i < 4; i++)
    {
        if (buffer[i] !=  signature[i])
        {
            printf("This is not a PDF\n");
            return 0;
        }
    }
    printf("It is a PDF!\n");

    fclose(input);
    return 0;
}
