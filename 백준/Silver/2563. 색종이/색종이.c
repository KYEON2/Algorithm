#include <stdio.h>

int main() {
    int area[100][100]= {0, };

    int n, r, h;
    int cnt = 0;
    scanf("%d", &n);
    for(int i=0; i<n; i++){
        scanf("%d %d", &r, &h);
        for(int m=100-(h+10); m<100-h; m++){
            for(int k=r; k<r+10; k++){
                area[m][k]=1;
            }
        }
    }
    for(int i=0; i<100; i++){
        for(int j=0; j<100; j++){
            if(area[i][j]==1){
                cnt ++;
            }
        }
    }
    printf("%d", cnt);
    return 0;
}