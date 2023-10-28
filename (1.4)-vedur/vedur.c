#include <stdio.h>

int main()
{
    int windspeed;
    int num_roads;
    int length = 100000;
    char road[length];
    int speed;


    scanf("%d", &windspeed);
    scanf("%d", &num_roads);

    for (int i = 0; i < num_roads; i++) {
        scanf("%s %d", road, &speed);

        if (speed < windspeed) {
            printf("%s lokud\n", road);
        } else
        {
            printf("%s opin\n", road);
        }
        

    }
}
