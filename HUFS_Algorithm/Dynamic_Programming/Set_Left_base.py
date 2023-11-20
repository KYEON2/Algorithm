W = int(input())
words = input().split()
# code below

dp = [[0 for j in range(len(words))] for i in range(len(words))]

#기본 세팅 
for j in range(len(words)):
    k = j
    pn = W - len(words[k])
    k -= 1
    while k > -1:
        pn -= len(words[k]) + 1
        k -= 1
    if pn < 0:
        dp[0][j] = -1
    else:
        dp[0][j] = pn ** 3

#dp 테이블 채우기 
for i in range(1,len(words)):
    minpn = dp[i-1][i-1]
    for l in range(i):
        if dp[l][i-1] < minpn and dp[l][i-1] > -1:
            minpn = dp[l][i-1]
    for j in range(i, len(words)):
        k = j
        pn = W - len(words[k])
        k -= 1
        while k > i-1:
            pn -= len(words[k]) + 1
            k -= 1
        if pn < 0:
            dp[i][j] = -1
        else:
            dp[i][j] = minpn + (pn**3)
        

#결과 출력하기 
result = dp[len(words)-1][len(words)-1]       
for i in range(len(words)-1):
    if dp[i][len(words)-1] != -1:
        if dp[i][len(words)-1] < result:
            result = dp[i][len(words)-1]
print(result)
