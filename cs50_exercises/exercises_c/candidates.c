#include <stdio.h>
#include <cs50.h>
#include <string.h>

typedef struct
{
    string name;
    int votes;
}candidate;

int main (void)
{
    candidate candidates[] = {{"Jose", 0}, {"Joao", 0}, {"Marcos",0}};
    for (int i = 0; i < 5; i++)
    {
        string vote = get_string("Em qual candidato voce vai votar? ");
        for (int j = 0; j < 3; j++)
        {
            if(strcmp(vote, candidates[j].name) == 0)
            {
                candidates[j].votes++;
            }
        }
    }
    int vencedor = 0;
    for(int k = 0; k < 3; k++)
    {
        if(candidates[k].votes > candidates[vencedor].votes)
        {
            vencedor = k;
        }
    }
    printf("O candidato mais votado foi %s com %i votos", candidates[vencedor].name, candidates[vencedor].votes);
}
