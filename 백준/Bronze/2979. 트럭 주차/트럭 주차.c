#include <stdio.h>

int arr[101];

int main (){
    int a, b, c, x, y;
    scanf("%d %d %d", &a, &b, &c);
    for (int i=0; i<3; i++){
        scanf("%d %d", &x, &y);
        for (int j=x; j<y; j++){
            arr[j] += 1;
        }
    }

    int sum = 0;
    for (int i = 1; i <101; i++){
        if(arr[i] == 1){
            sum += a*1;
        }
        else if (arr[i] ==2)
        {
            sum += b*2;
        }
        else if (arr[i] ==3)
        {
            sum += c*3;
        }
        
    }

    printf("%d", sum);

}