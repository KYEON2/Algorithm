W = int(input())
words = input().split()
# code below

#한 줄에 담을 시작 단어와 마지막 단어의 인덱스를 통해 만드는 dp테이블
#행 : 시작 단어의 words 리스트 안의 인덱스
#열 : 끝 단어의 words 리스트 안의 인덱스
#시작 단어의 인덱스 값이 끝 인덱스보다 큰 경우 없음
dp = [[0 for j in range(len(words))] for i in range(len(words))] #0으로 배열 초기화

#기본 세팅
#words 리스트에서 인덱스가 0인 첫 단어로 시작하는 상황 
for j in range(len(words)): # 끝 단어의 인덱스가 0부터 words 단어 개수 -1만큼 반복
	k=j
	pn = W - len(words[k]) # 패널티 값구하기(세제곱 하기 전 상태)
	k -= 1
 
    #여러개의 단어가 들어가서 띄어쓰기가 있는 경우
	while k > -1:
		pn -= len(words[k]) + 1 #띄어쓰기 -> +1
		k -= 1
	if pn < 0: #단어를 담았을 때 페이지 폭보다 길면
		dp[0][j] = -1 # 오류 상황
	else: #아니면
		dp[0][j] = pn ** 3 #세제곱
		
#dp 테이블 채우기
for i in range(1, len(words)):
	minpn = dp[i-1][i-1]
	for l in range(i):
		if dp[l][i-1] < minpn and dp[l][i-1] > -1:
			minpn = dp[l][i-1]
	for j in range(i, len(words)):
		k=j
		pn = W - len(words[k])
		k -= 1
		while k > i-1: 
			pn -= len(words[k]) + 1
			k-=1
		if pn < 0:
			dp[i][j] = -1
		else:
			dp[i][j] = minpn + (pn**3) #패널티 값 계산
	


#결과 출력하기 
result = dp[len(words)-1][len(words) -1]
for i in range(len(words)-1):
	if dp[i][len(words)-1] != -1:
		if dp[i][len(words)-1] < result:
			result = dp[i][len(words)-1]
print(result)

# dp[i][j]: i번째 단어부터 j번째 단어까지를 한 줄에 배치했을 때의 패널티로, i번째 단어 이전까지의 최소 패널티(minpn)에 i번째 단어부터 j번째 단어까지의 줄에 대한 패널티를 더한 값이다.
# n x n사이즈의 이중리스트를 만들었기 때문에 이중 for 문을 사용하여
# 시간복잡도는 O(n^2)


