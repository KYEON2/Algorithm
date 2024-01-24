n, a, b = map(int, input().split(' ')) #n명, a, b가 각각 몇번인지 입력

round = 0 #round 변수

while a != b: #a와 b가 같은 숫자라는 것은 같은 라운드인 것을 의미
    a -= a//2 
    b -= b//2 
    round += 1
    
print(round) #라운드 출력
