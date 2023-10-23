#include <stdio.h>

int main()
{
    int int_1;
    int int_2;
    int minutes;
    
    int printed_hour;
    int printed_minutes;

    scanf("%d %d", &int_1, &int_2);

    minutes = int_1 * 60 + int_2;
    minutes -= 45;

    printed_hour = (minutes)/60;
    printed_minutes = (minutes) % 60;

    if (printed_hour == 0 && printed_minutes < 45)
    {
        printed_hour = 23;
        printed_minutes += 60;
    }
    
    printf("%d %d", printed_hour, printed_minutes);

    return 0;
}