#include <stdio.h>

int main () {
    int n;
    int count = 0;
    scanf("%d", &n);

    while (n>0){
        if ( n == 64 ){
            n -= 64;
            count =1;
        }

        else if (32 <= n && n < 64){
            n -= 32;
            count += 1;
        }

        else if (16 <= n && n < 32){
            n -= 16;
            count += 1;
        }

        else if (8 <= n && n < 16){
            n -= 8;
            count += 1;
        }

        else if (4 <= n && n < 8){
            n -= 4;
            count += 1;
        }

        else if (2 <= n && n < 4){
            n -= 2;
            count += 1;
        }

        else {
            n -= 1;
            count += 1;
        }
        
    }

    printf("%d", count);
}