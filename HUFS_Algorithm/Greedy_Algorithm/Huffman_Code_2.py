#허프만 코드 계산 문제
#43 13 12 16 9 7을 입력받으면 최적 코드 트리의 cost 값을 도출함 (빈도수로 괄호쳐서 값 도출)
#결과 : 230 
import heapq

istr = input()

f = list(map(int, istr.split(' ')))
g = f
H=[]
count = 0
summ = 0
newint = ""

for i in range(len(f)):
	heapq.heappush (H, (f[i], str(g[i])))
	
while len(H) > 1:
	a = heapq.heappop(H)
	b = heapq.heappop(H)
	
	heapq.heappush(H,(a[0]+b[0], '('+a[1]+' '+b[1]+')'))
	
result = heapq.heappop(H)[1]

for k in range(len(result)):
	if result[k].isdigit():
		newint += result[k]
	else:
		if newint:
			summ += int(newint) * count
			newint = ""
		if result[k]=='(':
			count += 1
		elif result[k]==')':
			count -= 1
			
if newint:
    summ += int(newint) * count
	
	

print(summ)
