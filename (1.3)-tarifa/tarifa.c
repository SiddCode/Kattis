#include <stdio.h>

int main()
{
    int megabytes_per_month;
    int num_months;
    int megabyte_that_month;
    int i = 0;
    int sum = 0;

    scanf("%d", &megabytes_per_month);
    scanf("%d", &num_months);

    while (i < num_months) {
        scanf("%d", &megabyte_that_month);
        sum += (megabytes_per_month - megabyte_that_month);
        i += 1;
    }

    printf("%d", sum + megabytes_per_month);


    return 0;
}