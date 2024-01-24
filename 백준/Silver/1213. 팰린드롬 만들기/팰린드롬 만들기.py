#Greedy Algorithm

from collections import Counter #counter 모듈 사용

input = list(map(str, input()))
input.sort()

count = Counter(input) #각 문자가 몇 개인지 세주는 것

odd = 0
odd_alphabet = ''
result = ''

for i in count:
    if count[i] % 2 != 0: #문자가 홀수개이면
        odd += 1 
        odd_alphabet += i
        
    for _ in range (count[i]//2):
        result += i
            
if odd > 1: #홀수인 것이 하나보다 많으면
	print("I'm Sorry Hansoo") #회문을 만들 수 없음

elif odd == 0: #글자수가 짝수일 경우
	print(result + result[::-1])

else: #글자수가 홀수일 경우
	print(result + odd_alphabet + result[::-1])