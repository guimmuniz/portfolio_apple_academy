#include <cs50.h>
#include <stdio.h>
#include <string.h>

typedef struct
{
    string name;
    string number;
} person;

int main (void)
{
    person people[3];

    people[0].name = "David";
    people[0].number = "+123456";

    people[1].name = "John";
    people[1].number = "+98765";

    people[2].name = "Yulia";
    people[2].number = "+123456";

    string name = get_string("Name: ");

    for (int i = 0; i < 3; i++)
    {
        if (strcmp(people[i].name, name) == 0)
        {
            printf("%s's number is %s\n", name, people[i].number);
            return 0;
        }
    }
    printf("No number found!\n");
    return 1;
}
