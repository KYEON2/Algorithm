import sys
input = sys.stdin.readline

m, n = map(int, input().split())
arr = [0] + list(map(int, input().split()))

for i in range(1, m + 1):
    arr[i] += arr[i - 1]

result = []
for _ in range(n):
    i, j = map(int, input().split())
    result.append(str(arr[j] - arr[i - 1]))

sys.stdout.write('\n'.join(result))