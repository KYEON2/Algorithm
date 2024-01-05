#include <stdio.h>
#include <string.h>

int main (){
    char S[100] = {0, };
    scanf("%s", S);

    char alp[26] = {0, };
    int k = 0;

    int length = strlen(S);

    for (int i=0; i < length ; i ++){
        k= S[i] - 'a';
        alp[k] ++;
    }

    for (int j=0; j<26; j++){
        printf("%d ", alp[j]);
    }

}