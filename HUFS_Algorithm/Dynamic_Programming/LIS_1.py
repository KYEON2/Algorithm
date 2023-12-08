#최장 증가 부수열 문제 DP 알고리즘 1 -> 시간복잡도 O(n^2)
x = int(input())

arr = list(map(int, input().split()))

dp = [1 for i in range(x)] #dp[i]를 1로 초기화

for i in range(x):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))

#1. dp[i]의 값을 1로 초기화

#2. 현재 위치(i)보다 이전에 있는 원소(j)가 작은지 확인한다. (크거나 같으면 가장 긴 증가하는 부분 수열이 될 수 없음)

#3. 작다면, 현재 위치의 이전 숫자 중, dp 최댓값을 구하고 그 길이에 1을 더해주면 된다.

"""
예시 
arr | 10 20 10 30
dp  |  1  2  1  3
"""