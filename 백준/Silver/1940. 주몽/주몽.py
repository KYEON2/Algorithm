import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
listC = list(map(int,input().split()))

listC.sort() #listC를 정렬 함
left, right = 0, n - 1
count = 0

while left < right: #조건은 left가 right보다 항상 작아야함
    sum_num = listC[left] + listC[right]
    if sum_num < m: 
        left += 1
    elif sum_num > m:
        right -= 1
    else: #합이 m인 경우 
        count += 1
        left += 1
        right -= 1

print(count)