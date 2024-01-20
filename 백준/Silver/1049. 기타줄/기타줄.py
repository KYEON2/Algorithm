#Greedy Algorithm

n, m = map(int,input().split(' ')) #고장난 개수 n, 제품의 개수 m을 입력받음

setP = [] #세트가격
oneP = [] #낱개가격

for _ in range(m): #세트, 낱개가격 입력받음
    a, b = map(int,input().split(' '))
    setP.append(a)
    oneP.append(b)
    
setP = min(setP) #최솟값 찾기
oneP = min(oneP) #최솟값 찾기

if setP >= oneP * 6: #세트 가격이 최소 낱개가격x6보다 비싼 경우
    print(n * oneP) #낱개로 구매
    
else:
    if setP < (n%6) * oneP: #세트로 구매하고 남은 개수를 세트로 샀을 때 더 싼 경우
        print( (n // 6 + 1)*setP ) #세트를 하나 더 구매
    else: #세트보다 낱개가 더 싼 경우
        print(( n // 6 )*setP + (n%6) * oneP) #낱개로 구매 
        
