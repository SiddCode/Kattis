#include <stdio.h>

int main()
{
    float x;
    float option_1;
    float option_2;

    scanf("%f", &x);

    option_1 = 1/ (x/100);
    option_2 = 1/ (1-x/100);

    printf("%f\n", option_1);
    printf("%f", option_2);


    return 0;
}