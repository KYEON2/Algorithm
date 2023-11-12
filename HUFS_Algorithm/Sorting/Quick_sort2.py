# 추가점수 1 - Quick Sort
#퀵소트에 비해 비교 및 스왑 횟수가 적기 때문에 작은 배열의 경우 삽입 정렬이 퀵 정렬보다 효율적
#굳이 하나가 남을 때까지 분할할 필요는 없으니까 10과 40 사이의 상수 k에 대해서, k개 이하가 되면 insertion sort정렬을 하면 더 빠름
"""def insertion_sort(A, first, last):
	global Qc2, Qs2, Qc3, Qs3
	for i in range(first+1,last+1):
		Qc2 += 1
		Qc3 += 1
		j = i-1
		while A[j+1] < A[j] and j >= first:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1
			Qs2 += 1
			Qs3 += 1
   
def quick_sort2(A, first, last):
	global Qc2, Qs2 #비교, swqp 횟수
	
	if (last - first+1) >= 10 and (last - first+1) <= 40:
		insertion_sort(A, first, last)
		return
	
	if first >= last: return
	left, right = first + 1, last
	pivot = A[first]
	
	while left <= right:
		while left <= last and A[left]<pivot:
			left += 1
			Qc2 += 1
		while right > first and A[right] > pivot:
			right -= 1
			Qc2 += 1
		if left <= right:
			A[left], A[right] = A[right], A[left]
			left += 1
			right -= 1
			Qs2 += 1
			
		A[first], A[right] = A[right], A[left]
		Qs2 += 1
		
		quick_sort2(A,first, right -1)
		quick_sort2(A,right + 1, last)"""
  
  
  
  
def insertion_sort1(A, first, last):
	global Qc2, Qs2
	for i in range(first+1, last+1):
		Qc2 += 1
		j = i-1
		while A[j+1] < A[j] and j >= first:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1
			Qs2 += 1
   
def quick_sort2(A, first, last):  #추가 점수 1
	global Qc2,Qs2
	if first >= last:return
	if (last-first) < 40 and (last-first) > 10:
		insertion_sort1(A,first, last)
		return
	left, right = first+1, last
	pivot = A[first]
	while left <= right:
		while left <= last and A[left] < pivot:
			Qc2 += 1 
			left += 1
		while right > first and A[right] >= pivot:
			Qc2 += 1
			right -= 1
		if left <= right: # swap A[left] and A[right]
			A[left], A[right] = A[right], A[left]
			Qs2 += 1
			left += 1
			right -= 1
		# place pivot at the right place
	A[first], A[right] = A[right], A[first]
	Qs2 += 1

	quick_sort2(A, first, right-1)
	quick_sort2(A, right+1, last)
	