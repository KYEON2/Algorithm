n = input ()

A = input().split(' ') #빈칸을 기준으로 
A = [int(i) for i in A] #A에 있는 내용을 정수로 바꿔줌

sorted_A = [i for i in A] #A를 sorted_A에 똑같이 넣음
sorted_A.sort() #sorted_A를 오름차순으로 정렬 
#sorted_A = sorted(A)로 위 두 줄을 대체할 수도 있음

p = [] #새로운 배열

for i in A:
    p.append(sorted_A.index(i)) #A에 있는 i를 sorted_A의 몇 번째인지 찾고 p배열에 넣어줌
    sorted_A[sorted_A.index(i)] = -1 #중복되는 것을 모두 번호에 넣기 위해 이 과정이 필요
    
    
for result in p:
    print(str(result), end=' ') #result는 정수라서 문자열로 바꿔줘야 함
    
    




