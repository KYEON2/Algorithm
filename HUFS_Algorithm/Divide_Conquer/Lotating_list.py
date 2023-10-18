
# 분할정복 알고리즘 코드를 이용하여 리스트 A와 시작, 마지막 번째 위치를 가지고 함수 작성
# 이진탐색 활용

# O(logN)
def Rotating(A, start, last):
	if start == last: # 시작값과 마지막 값이 같다면 첫번째 값 출력
		return start # last 넣어도 똑같음
	
	mid = (start + last) // 2 # 분할정복을 해야하므로 가운데 mid 값 지정
	
	if A[mid] < A[last]: # 이진탐색 사용 
		return Rotating(A, start, mid) # A[0] ~ A[mid-1] 사이에 존재함
	else:
		return Rotating(A, mid + 1, last) # A[mid+1] ~ A[last] 사이에 존재함

A = list(map(int, input().split())) # 리스트 A 값 입력
k = len(A) - Rotating(A, 0, len(A)-1) # 함수 파라미터에 리스트 A, 시작 값 0, 마지막 값 len(A)-1

if len(A) == k: # 오름차순 일때
   k = 0
		
print(k)#이진 탐색이 두번 사용 되면서 리스트의 크기를 절반으로 줄여주기 때문에 시간복잡도는 O(logN)을 갖는다