#include <stdio.h>

int main()
{
    int user_input;
    int first_digit;
    int second_digit;

    scanf("%d", &user_input);

    first_digit = user_input / 10;
    second_digit = user_input % 10;

    printf("%d", second_digit*10 + first_digit);


    return 0;
}