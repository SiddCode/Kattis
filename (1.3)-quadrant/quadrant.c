
#include <stdio.h>

int main()
{
    int x_coord;
    int y_coord;

    scanf("%d", &x_coord);
    scanf("%d", &y_coord);

    if (x_coord > 0 && y_coord > 0) {
        printf("1");
    } else if (x_coord < 0 && y_coord > 0)
    {
        printf("2");
    } else if (x_coord < 0 && y_coord < 0)
    {
        printf("3");
    } else
    {
        printf("4");
    }
    

    return 0;
}