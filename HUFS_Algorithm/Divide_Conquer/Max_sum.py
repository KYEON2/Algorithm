#시간복잡도 O(nlogn)

def max_sum(A, left, right):
	# A[left], ..., A[right] 중 최대 구간 합 리턴

	if left ==right:
		return A[left]
	
	mid = (left + right) // 2
	#A[i...mid]와 A[mid+1...right]의 형태를 갖는 구간의 합으로 이루어짐
	
	#중간에 걸친 경우, 왼쪽 최대합
	#A[i...mid]형태를 갖는 최대 구간을 찾음
	i = mid
	sum = 0
	left_part = -1000
	while (i>=left):
		sum += A[i]
		left_part = max(left_part,sum)
		i -= 1
		
	#중간에 걸친 경우, 오른쪽 최대합
	#A[mid+1...j]형태를 갖는 최대 구간을 찾음
	j = mid +1
	sum = 0
	right_part = -1000
	while (j <= right):
		sum += A[j]
		right_part = max(right_part, sum)
		j += 1
		
	#걸치지 않고 양분된 구간 내에 속하는 경우
	#최대 구간이 두 부분 중 하나에만 속해있는 경우의 답을 재귀로 찾음
	single = max(max_sum(A, left, mid), max_sum(A, mid +1, right))
	
	#중간에 걸친 경우와 걸치지 않은 경우 중 높은 값을 반환
	#최대 구간 반환
	return max(left_part + right_part, single)

A = [int(x) for x in input().split()]
sol = max_sum(A, 0, len(A)-1)
print(sol)