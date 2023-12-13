#히스토그램에서 가장 큰 직사각형 구하기
#백준 6549번 문제 -> 시간복잡도 O(n)

from collections import deque
import sys

while True:
    rec=list(map(int, sys.stdin.readline().split()))
    n=rec.pop(0)
    
    if n==0:
        break
    
    stack = deque()
    answer = 0
    
    #왼쪽부터 차례대로 탐색
    for i in range(n):
        while len(stack) != 0 and rec[stack[-1]] > rec [i]:
            tmp = stack.pop()
            
            if len(stack) == 0:
                width = i
            else:
                width = i - stack[-1] -1
            answer = max(answer, width * rec[tmp])
        stack.append(i)
        
    #스택에 남아있는 것 처리 // 넓이 계산
    while len(stack) != 0:
        tmp = stack.pop()
        
        if len(stack) == 0:
            width = n
        else:
            width = n - stack[-1] -1
            
        answer = max(answer, width*rec[tmp])
    print(answer)