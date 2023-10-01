#include <stdio.h>
#include <string.h>

int isGroupWord(char *word) {
    int alphabet[26] = {0}; // 알파벳 개수를 저장할 배열 초기화

    int len = strlen(word);
    for (int i = 0; i < len; i++) {
        char currentChar = word[i];
        if (alphabet[currentChar - 'a'] == 1) {
            // 이미 나온 문자인 경우
            if (i > 0 && word[i - 1] != currentChar) {
                return 0; // 그룹 단어가 아님
            }
        } else {
            alphabet[currentChar - 'a'] = 1; // 문자 등장 표시
        }
    }
    return 1; // 그룹 단어
}

int main() {
    int N;
    scanf("%d", &N); // 단어의 개수 입력

    int count = 0;
    for (int i = 0; i < N; i++) {
        char word[101]; // 단어의 최대 길이를 100으로 가정
        scanf("%s", word);

        if (isGroupWord(word)) {
            count++;
        }
    }

    printf("%d\n", count);

    return 0;
}