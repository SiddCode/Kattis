#include <stdio.h>

int main()
{
    float a[14] = {0,0,1,2,3,4,5,6,5,4,3,2,1};

    int num_house;
    int moves_away;
    float sum = 0;


    scanf("%d", &num_house);

    for (int i = 0; i < num_house; i++){

        scanf("%d", &moves_away);

        sum += (a[moves_away] / 36);

    }

    printf("%f", sum);
}
