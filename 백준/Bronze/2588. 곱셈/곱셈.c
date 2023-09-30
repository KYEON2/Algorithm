#include <stdio.h>

int main ( ){
    int A;
    char B[4];
    int X1, X2, X3, result = 0;

    scanf("%d", &A);
    getchar();
    scanf("%s", B);


    int Y1 = B[0] - '0';
    int Y2 = B[1] - '0';
    int Y3 = B[2] - '0';

    X1 =  A * Y1;
    X2 =  A * Y2;
    X3 =  A * Y3;

    result = X3 + 10 * X2 +100 * X1;

    
    printf("%d\n", X3);
    printf("%d\n", X2);
    printf("%d\n", X1);
    printf("%d\n", result);
}