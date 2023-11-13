# 추가점수 2 - Quick Sort
# 적당한 k개가 남을 때까지 분할한 후, 따로 insertion sort등으로 정렬하지 않고 재귀를 한다면, 전체값이 완전히 정렬되지 않음
# 정렬을 완료하기 위해, 전체 값들을 대상으로 insertion sort를 이용하면 정렬을 완료할 수 있음

def insertion_sort2(A, first, last):
	global Qc3, Qs3
	for i in range(first+1, last+1):
		Qc3 +=1
		j = i-1
		while A[j+1] < A[j] and j >= first:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1
			Qs3 += 1
	
 
 
def quick_sort3(A, first, last):
	global Qc3, Qs3 #비교, swqp 횟수
	
	if first >= last: return
	left, right = first+1, last
	pivot = A[first]
	while left <= right:
		while left <= last and A[left] < pivot:
			Qc3 += 1
			left += 1
		while right > first and A[right] >= pivot:
			Qc3 += 1
			right -= 1
		if left <= right: # swap A[left] and A[right]
			A[left], A[right] = A[right], A[left]
			Qs3 += 1
			left += 1
			right -= 1
		# place pivot at the right place
	A[first], A[right] = A[right], A[first]
	Qs3 += 1

	if (last-first)>10 and (last-first)<40:
		insertion_sort2(A, first, last)
	else:
		quick_sort3(A, first, right-1)
		quick_sort3(A, right+1, last)