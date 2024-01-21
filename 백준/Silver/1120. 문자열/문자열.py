n, m = input().split(' ')

answer = []

for i in range(len(m)-len(n)+1):
    count = 0
    for j in range(len(n)):
        if n[j] != m [i+j]: #각 글자랑 다를 경우 count 함
            count += 1
    answer.append(count)
    
print(min(answer)) #answer중 가장 작은 값
