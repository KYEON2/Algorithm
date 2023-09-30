import heapq 

# 최소힙, 최대힙
def findk(A): # O(nlogn) -> for 문 한번 사용해서 O(n), heapq모듈 중에 heappop, heappush 사용 해서 n *logn
	
	# 최소힙, 최대힙 사용
	result = []
	max_heap, min_heap = [], [] 
	
	for i in range(len(A)):
		k = i//3+1 #k범위 설정
		
		#max_heap이 비어있거나, max_heap의 루트값보다 A[i]값이 작다면 -A[i] 삽입
		if not max_heap or -max_heap[0] >= A[i]:
			heapq.heappush(max_heap, -A[i]) #최대힙
			#파이썬의 heapq는 최대힙이 없기 때문에 부호를 사용하여 최대힙을 구현
			#부호 바꿔서 넣은 후, heappop을 할 때 부호 바꾸면 최대힙과 동일
			
			
		# 다른 경우에는 min_heap에 A[i]삽입
		else:
			heapq.heappush(min_heap, A[i]) #최소힙
			
		#max_heap의 루트노드를 k번째 작은 수로 만들기 위해 max_heap의 크기를 k개로 유지함
		if len(max_heap) > k: # 최대힙의 크기가 k 번째 작은 수의 값보다 크면
			heapq.heappush(min_heap, -heapq.heappop(max_heap)) #최소힙에 넣음
		elif len(max_heap) < k and min_heap: #최대힙의 크기가 k 값보다 작고, 최소힙이면
			heapq.heappush(max_heap, -heapq.heappop(min_heap)) #최대힙에 넣음
			
		result.append(-max_heap[0]) #루트노드는 k번째 작은 수이며, 부호를 바꿔서 append함
	return result 

A = list(map(int, input().split())) #A리스트 입력 받음
K = findk(A) 
print(sum(K)) #값들을 더함
