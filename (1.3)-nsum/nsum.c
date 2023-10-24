#include <stdio.h>

int main()
{
    int num_integers;
    int next_integer;
    int sum = 0;
    
    scanf("%d", &num_integers);
    
    for(int i = 0; i < num_integers; i++) {
        scanf("%d", &next_integer);
        
        sum += next_integer;
        
    }
    
    printf("%d", sum);

    return 0;
}