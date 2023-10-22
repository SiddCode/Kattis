#include <stdio.h>

int main()
{
    int line_one, line_two;

    scanf("%d", &line_one);
    scanf("%d", &line_two);

    printf("%d", 2022 + line_one/line_two);

    return 0;
}