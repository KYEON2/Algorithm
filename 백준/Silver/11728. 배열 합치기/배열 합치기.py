import sys

input = sys.stdin.readline

m, n = map(int, input().split())
q = list(map(int, input().split()))
p = list(map(int, input().split()))

q.extend(p)
q.sort()

print(*q)