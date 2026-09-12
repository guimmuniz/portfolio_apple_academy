#include <stdio.h>
#include <stdlib.h>

const int block = 512;

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./recover FILE\n");
        return 1;
    }

    FILE *card = fopen(argv[1], "r");

    if (card == NULL)
    {
        printf("Couldn't open the file!");
    }

    uint8_t buffer[block];

    while(fread(buffer, 1, block, card) == block)
    {
        if (buffer[0]==0xff && buffer[1]==0xd8 && buffer[2]==0xff && (buffer[3] & 0xf0)==0xe0)
        {
            sprintf(filename, "03i.jpg", 2);
            FILE *img = fopen(filename, "w");

            fwrite(buffer, 1, block, img);
        }
    }

    fopen(card);
}
