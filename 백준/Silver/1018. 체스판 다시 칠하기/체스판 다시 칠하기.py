n, m = map(int, input().split())

board = [] #입력받은 체스판
result = [] #수정한 체스판

for _ in range(n):
    board.append(input()) # 체스판을 입력받음
    
for i in range(n-7):
    for j in range(m-7):
        change1 = 0 #첫 시작이 B일 경우
        change2 = 0 #첫 시작이 W일 경우
        
        for a in range(i, i+8):
            for b in range(j, j+8):
                if (a+b)%2 == 0:
                    if board[a][b] != 'B':
                        change1 += 1
                    if board[a][b] != 'W':
                        change2 += 1
                
                else:
                    if board[a][b] != 'W':
                        change1 += 1
                    if board[a][b] != 'B':
                        change2 += 1
        result.append(change1)
        result.append(change2)
        
print(min(result)) #모든 경우의 최솟값을 구해줌
                    
    
