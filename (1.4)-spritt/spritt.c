#include <stdio.h>

int main()
{
    int num_classrooms;
    int num_bottles;
    int classroom_bottle;
    int sum = 0;

    scanf("%d %d", &num_classrooms, &num_bottles);

    for(int i = 0; i < num_classrooms; i++){
        scanf("%d", &classroom_bottle);
        sum += classroom_bottle;
    }

    if (sum <= num_bottles)
    {
        printf("Jebb");
    } else
    {
        printf("Neibb");
    }
    
    

    return 0;
}