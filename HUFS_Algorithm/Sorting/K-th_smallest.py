# 최소힙, 최대힙 2개 사용

import heapq # O(nlogn) -> for문 한번 사용 o(n), heapq 모듈 중 heappop, heappush 사용하여서 n * logn 

# 최소힙, 최대힙 둘 다 사용
def findkth(A):
	result = []
	max_heap, min_heap = [], [] # max, min heap
	
	for i in range(len(A)):
		k = i//3+1 # k 범위 설정
		
		# max_heap이 비어있거나, max_heap의 루트값보다 i값이 작거나 같다면, -i 삽입
		if not max_heap or -max_heap[0] >= A[i]:
			heapq.heappush(max_heap, -A[i]) # 최대힙 생성
			# 파이썬의 heapq는 최대힙을 제공하지 않기 때문에 부호를 변경하는 방법을 사용하여 최대힙 구현
			# 부호를 바꿔서 넣어준 이후에 heappop을 해줄때 부호를 바꾸면 최대힙과 동일해짐
			
		# 그 외에는 min_heap에 i 삽입
		else:
			heapq.heappush(min_heap, A[i]) # 최소힙 생성
			
		 # min_heap의 루트노드를 k번째 작은 수로 만들기 위하여 min_heap의 크기를 k개로 유지
		if len(max_heap) > k: # 최대힙의 크기가 k번째 작은 수의 값보다 크다면
			heapq.heappush(min_heap, -heapq.heappop(max_heap)) # 최소힙에 넣어줌
		elif len(max_heap) < k and min_heap: # k번째 작은 수의 값보다 크거나, 최소힙이 있으면
			heapq.heappush(max_heap, -heapq.heappop(min_heap)) # 최대힙에 넣어줌
			
		result.append(-max_heap[0]) # 루트 노드 == k번째 작은수, 부호를 바꾸면서 append
		
	return result # k번째 작은 수를 저장한 result 리스트 반환

A = list(map(int, input().split())) # A 리스트 입력
M = findkth(A) # k번째 작은수 찾는 함수 호출하여 result 리스트를 M으로 반환
print(sum(M)) # M값 합
