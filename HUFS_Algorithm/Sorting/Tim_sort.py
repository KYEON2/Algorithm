# python의 sort 함수는 Tim sort 알고리즘을 구현한 것
def insertion_sort3(A, first, n): #Tim sort 를 위한 insertion_sort3 함수
	global Mc2, Ms2
	for k in range(first + 1, n + 1):
		val = A[k]
		w = k
		while w > first and A[w-1]>val:
			Mc2 += 1
			A[w] = A[w-1]
			Ms2 += 1
			w -= 1
		A[w]= val
		
		
# 추가점수 4 - Tim Sort
def merge_sort2(A, first, last):
	if first >= last : return
	merge_sort2(A, first, (first+last)//2)
	merge_sort2(A, (first+last)//2+1, last)
	merge_two_sorted_lists2(A, first, last)
	
def merge_two_sorted_lists2(A, first, last):
	global Mc2, Ms2
	if (last - first + 1) >= 10 and (last - first +1) <= 40:
		insertion_sort3(A, first, last)
		return
	if first >= last:
		return
	
	m = (first + last) // 2
	i, j = first, m+1
	B = list()
	while i <= m and j <= last:
		if A[i] <= A[j]:
			Mc2 += 1
			B.append(A[i])
			Ms2 += 1
			i += 1
		else: 
			Mc2 += 1
			B.append(A[j])
			Ms2 += 1
			j += 1
	
	for k in range(i, m+1):
		B.append(A[k])
		Ms2 += 1
	for k in range(j, last+1):
		B.append(A[k])
		Ms2 += 1
	for k in range(first, last+1):
		A[k] = B[k-first]
		Ms2 += 1