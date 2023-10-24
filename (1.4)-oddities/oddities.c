int main()
{
    int num_int;
    int user_input;
    
    scanf("%d", &num_int);
    
    int arr[num_int];
    
    
    for(int i = 0; i < num_int; i++){
        scanf("%d", &user_input);
        
        arr[i] = user_input;
        
    }
    
    
    for(int i = 0; i < num_int; i++){
        if (arr[i] % 2 == 0) {
            printf("%d is even\n", arr[i]);           
        } else {
            printf("%d is odd\n", arr[i]);
        }

    }
    

    return 0;
}