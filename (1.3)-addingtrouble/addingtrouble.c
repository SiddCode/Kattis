#include <stdio.h>

int main()
{
    int first_digit;
    int second_digit;
    int third_digit;

    scanf("%d %d %d", &first_digit, &second_digit, &third_digit);

    if (first_digit + second_digit == third_digit)
    {
        printf("correct!");
    } else
    {
        printf("wrong!");
    }
    

    return 0;
}