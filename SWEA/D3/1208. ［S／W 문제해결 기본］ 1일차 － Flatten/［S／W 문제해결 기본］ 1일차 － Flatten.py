T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    k = int(input())
    arr = list(map(int, input().split()))
    
    for i in range (k) :
        p = arr.index(max(arr))
        q = arr.index(min(arr))
        
        arr[p] -= 1
        arr[q] += 1
        
    result = max(arr) - min(arr) 
    
    print(f"#{test_case} {result}")
    