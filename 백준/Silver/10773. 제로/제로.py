m = int(input())
a = []

for i in range(m):
    x = int(input())

    if x == 0:
        if a:          # 리스트가 비어있지 않을 때만 pop
            a.pop()
    else:
        a.append(x)

print(sum(a))