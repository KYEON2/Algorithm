import sys

input = sys.stdin.readline

n, m = map(int, input().split()) #입력받은 두 수를 나누어 n과 m에 넣어줌

dict = {} #새로운 배열 생성 

for i in range(1, n + 1): #n번 입력을 받아 각 번호에 단어를 넣음
    a = input().rstrip()
    dict[i] = a
    dict[a] = i

for i in range(m): #m번 출력하고 싶은 단어나 번호를 넣어 
    quest = input().rstrip()
    if quest.isdigit(): #숫자면 문자를 출력하고
        print(dict[int(quest)])
    else: #문자면 숫자를 출력함
        print(dict[quest])