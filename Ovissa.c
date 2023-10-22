#include <stdio.h>

int main()
{
    
    char c;
    int counter = 0;

    for (;;) {
        
        if (getchar() != 'u') {
            break;
        }

        counter += 1;

    }
    
    printf("%d", counter);

    return 0;
}