#허프만 코드 계산 문제
#43 13 12 16 9 7을 입력받으면 괄호친 값을 도출함 (빈도수 말고 문자번호로 괄호쳐줌)
#(0 ((2 1) ((5 4) 3)))
import heapq

istr = input()

f = list(map(int, istr.split(' ')))

H=[]
count = 0
summ = 0

for i in range(len(f)):
	heapq.heappush (H, (f[i], str(i))) #
	
while len(H) > 1:
	a = heapq.heappop(H)
	b = heapq.heappop(H)
	
	heapq.heappush(H,(a[0]+b[0], '('+a[1]+' '+b[1]+')'))
	
result = heapq.heappop(H)[1]

for k in range(len(result)):
	if (result[k]=='('):
		count += 1
	elif (result[k]==')'):
		count -= 1
	elif result[k].isdigit():
		summ += int(result[k]) * count

print(result)
