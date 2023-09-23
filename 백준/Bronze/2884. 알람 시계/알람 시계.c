#include <stdio.h>

int main (){
    int H, M;

    scanf("%d %d", &H, &M);

    if (M < 45) {
        int M1 = 45-M;
        M = 60 - M1;

        if (H == 0){
            H = 23;
        }
        else {
            H -= 1;
        }
    }
    else {
        M = M - 45;
    }
    printf("%d %d",H,M);

    return 0;
}