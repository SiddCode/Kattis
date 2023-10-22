#include <stdio.h>

int main()
{
    int num_of_rods;
    int length;
    int sum = 0;

    scanf("%d", &num_of_rods);

    for (int i = 0; i < num_of_rods; i++){
        scanf("%d", &length);
        sum += length;
    }

    printf("%d", sum - (num_of_rods - 1));

    return 0;
}