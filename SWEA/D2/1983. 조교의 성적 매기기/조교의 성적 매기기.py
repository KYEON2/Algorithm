T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    arr = []
    score = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
    
    for i in range(1,n+1) :
        a, b, c = map(int, input().split())
        arr.append(a*0.35 + b*0.45 + c *0.2)
        
        if i == k:
            total = arr[-1]
        
    arr.sort(reverse=True)
    for i in range (n) :
        if arr[i] == total :
            k = i
            break
    
    p = n // 10
    result = score[k // p]
    
    print(f"#{test_case} {result}")
    
    
