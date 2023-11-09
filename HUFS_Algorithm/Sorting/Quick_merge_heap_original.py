import random, timeit

##
## 여기에 세 가지 정렬함수를 위한 코드를...
##

# 힌트에 global을 쓰라는 이유는 머지소트에서 함수가 2개, 힙소트에서 함수가 3개 사용되기 때문에 global 사용하면 될듯

# Tim Sort 구현해볼것 - merge + insertion
# - 추가점수용 비교해보고 싶은 알고리즘 insertion + binary search, insertion_binary_sort
# merge + insertion 

def insertion_binary_sort(A): # 삽입 + 이진탐색 정렬
	# 최악의 경우 O(n^2) 
	# average O(n^2), 최고 O(nlogn)
	# 비교횟수O(nlogn) + 이동횟수O(n^2) = O(n^2)
	# comparison에 비해 swap이 굉장히 많이 일어남을 볼 수 있음
	
	
	global Qc4, Qs4 # 비교, swap 횟수
	
	for i in range(len(A)):
		j = i-1
		select = A[i]
		
		loc = binary_search(A, 0, j, select)
		
		while (j >= loc):
			A[j+1] = A[j]
			j -= 1
			Qs4 += 1 # 한칸씩 뒤로 미룸
		A[j+1] = select
		
		
def binary_search(A, left, right, x):
	global Qc4, Qs4 # 비교, swap 횟수
	
	while (left <= right):
		m = left + (right - left) // 2
		if (x == A[m]):
			Qc4 += 1
			return m + 1
		elif (x > A[m]):
			left = m + 1
			Qc4 += 1
			Qs4 += 1
		else:
			right = m - 1
			Qc4 += 1
			Qs4 += 1
	return left

# Quick, merge, heap
def quick_sort(A, first, last): # in-place, unstable
	
	global Qc, Qs # 비교, swap 횟수
	
	if first >= last: return
	left, right = first + 1, last
	pivot = A[first] # 첫 번째 값 pivot
	while left <= right: # pivot보다 작은 값은 왼쪽, 큰 값은 오른쪽
		while left <= last and A[left] < pivot:
			left += 1
			Qc += 1
		while right > first and A[right] > pivot:
			right -= 1
			Qc += 1
		if left <= right: # swap A[left] and A[right]
			A[left], A[right] = A[right], A[left]
			Qs += 1
			left += 1
			right -= 1
			
	A[first], A[right] = A[right], A[first] # pivot을 제 위치로 보냄 (Pivot과 first를 바꾸기 위함)
	Qs += 1
	
	quick_sort(A, first, right - 1) # pivot보다 작은 것들을 재귀 정렬
	quick_sort(A, right + 1, last) # pivot보다 큰 값들을 재귀 정렬

def insertion_sort(A, first, last):
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
	
#추가점수 1 - Quick Sort
#퀵소트에 비해 비교 및 스왑 횟수가 적기 때문에 작은 배열의 경우 삽입 정렬이 퀵 정렬보다 효율적
def quick_sort2(A, first, last): # in-place, unstable
	global Qc2, Qs2 # 비교, swap 횟수
	
	if (last - first+1) >= 10 and (last - first+1) <= 40: # 10 ~ 40가 되었을 때
		insertion_sort(A, first, last) # 분할을 멈추고 insertion_sort
		return

	if first >= last: return
	left, right = first + 1, last
	pivot = A[first] # 첫 번째 값 pivot

	while left <= right: # pivot보다 작은 값은 왼쪽, 큰 값은 오른쪽
		while left <= last and A[left] < pivot:
			left += 1
			Qc2 += 1
		while right > first and A[right] > pivot:
			right -= 1
			Qc2 += 1
		if left <= right: # swap A[left] and A[right]
			A[left], A[right] = A[right], A[left]
			left += 1
			right -= 1
			Qs2 += 1
			
	A[first], A[right] = A[right], A[first] # pivot을 제 위치로 보냄 (Pivot과 first를 바꾸기 위함)
	Qs2 += 1
	
	quick_sort2(A, first, right - 1) # pivot보다 작은 것들을 재귀 정렬
	quick_sort2(A, right + 1, last) # pivot보다 큰 값들을 재귀 정렬
	
#추가점수 2 - Quick Sort3
#퀵소트에 비해 비교 및 스왑 횟수가 적기 때문에 작은 배열의 경우 삽입 정렬이 퀵 정렬보다 효율적
def quick_sort3(A, first, last): # in-place, unstable
	global Qc3, Qs3 # 비교, swap 횟수
	
	# 적당한 K개가 남을 때까지만 분할하라고 했는데 K개의 범위가 주어지지 않았습니다.
	# 1번과 똑같다고 저는 생각하게 되어서 똑같이 작성했습니다.
	if (last - first+1) >= 10 and (last - first+1) <= 40: # 10 ~ 40가 되었을 때
		insertion_sort(A, first, last) # 분할을 멈추고 insertion_sort
		return

	if first >= last: return
	left, right = first + 1, last
	pivot = A[first] # 첫 번째 값 pivot

	while left <= right: # pivot보다 작은 값은 왼쪽, 큰 값은 오른쪽
		while left <= last and A[left] < pivot:
			left += 1
			Qc3 += 1
		while right > first and A[right] > pivot:
			right -= 1
			Qc3 += 1
		if left <= right: # swap A[left] and A[right]
			A[left], A[right] = A[right], A[left]
			left += 1
			right -= 1
			Qs3 += 1
			
	A[first], A[right] = A[right], A[first] # pivot을 제 위치로 보냄 (Pivot과 first를 바꾸기 위함)
	Qs3 += 1
	
	quick_sort3(A, first, right - 1) # pivot보다 작은 것들을 재귀 정렬
	quick_sort3(A, right + 1, last) # pivot보다 큰 값들을 재귀 정렬
	

def merge_sort(A, first, last):
	
	global Ms # 교환 or 이동 횟수
	
	if first >= last: return
	merge_sort(A, first, (first+last)//2)
	merge_sort(A, (first+last)//2+1, last)
	merge_two_sorted_lists(A, first, last)
	
def merge_two_sorted_lists(A, first, last):
	
	global Mc, Ms # 비교 횟수, 이동횟수
	
	m = (first + last) // 2
	i, j = first, m + 1
	B = []
	while i <= m and j <= last:
		Mc += 1
		if A[i] <= A[j]:
			B.append(A[i])
			i += 1
		else:
			B.append(A[j])
			j += 1
	for k in range(i, m+1):
		B.append(A[k])
		Ms += 1 # 비교 안함, 남는 값 그대로 이동
	for k in range(j, last+1):
		B.append(A[k])
		Ms += 1 # 비교 안함, 남는 값 그대로 이동
	for i in range(first, last+1):
		A[i] = B[i-first]
		Ms += 1 # B에서 A로 이동





def heapify(A, k, n): # rebuildHeap (혹은 downHeap)라고도 함, O(logN)
# A: 완전이진트리를 나타내는 배열
# i: 배열 인덱스 (노드 번호)
# n: 정렬할 원소들 개수 (완전이진트리 크기)

	global Hc, Hs # 비교, 교환 or 이동 횟수
	
	if n == 0: # heap이 비어있으면 
		return None
	while 2*k+1 < n:
		L,R = 2*k+1,2*k+2
		if L < n and A[k] < A[L]:
			m = L
			Hc += 1
		else:
			m = k
			Hc += 1
		if R < n and A[m] < A[R]:
			m = R
			Hc += 1
		if m != k:
			A[k],A[m] = A[m],A[k]
			k = m
			Hs += 1
		else:
			break

def makeHeap(A): # O(nlogn)
	n = len(A)
	for k in range(n//2-1, -1, -1):
		heapify(A, k, n) # O(log n)
	
# 힙 정렬
def heap_sort(A):
	
	global Hc, Hs # 비교, 교환 or 이동 횟수
	
	n = len(A)
	# 단계 1 - O(n log n)
	makeHeap(A)

	# 단계 2 - O(n log n)
	for i in range(n-1, -1, -1):
		A[0], A[i] = A[i], A[0]
		Hs += 1
		n -= 1
		heapify(A, 0, n) # O(log n)
		
	
	
def insertion_sort2(A, first, n): #위의 insrtion_sort와 같은 코드지만 merge_sort와 quick_sort에서 비교횟수와 스압(이동)횟수 분석을 위해 같은 코드를 하나 더 작성 
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

# merge_sort와 insertion 합침	 -> Tim sort
def merge_sort2(A, first, last):
	if first >= last: return
	merge_sort2(A,first,(first+last)//2)
	merge_sort2(A,(first+last)//2+1,last)
	merge_two_sorted_lists2(A,first,last)
	
def merge_two_sorted_lists2(A, first, last):
	global Mc2, Ms2
	if (last - first + 1) >= 10 and (last - first+1) <= 40:			#들어온 구간이 조건에 해당되면 insertion_sort로 정렬실행
		insertion_sort2(A,first,last)
		return
	if first >= last:
		return

	m = (first + last)//2
	i,j = first, m+1
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
			
	for k in range(i,m+1):
		B.append(A[k])
		Ms2 += 1
	for k in range(j,last+1):
		B.append(A[k])
		Ms2 += 1
	for k in range(first,last+1):
		A[k]=B[k-first]
		Ms2 += 1


# 아래 코드는 바꾸지 말 것!
# 직접 실행해보면, 어떤 값이 출력되는지 알 수 있음
#

def check_sorted(A):
	for i in range(n-1):
		if A[i] > A[i+1]: return False
	return True

#
# Qc는 quick sort에서 리스트의 두 수를 비교한 횟수 저장
# Qs는 quick sort에서 두 수를 교환(swap)한 횟수 저장
# Mc, Ms는 merge sort에서 비교, 교환(또는 이동) 횟수 저장
# Hc, Hs는 heap sort에서 비교, 교환(또는 이동) 횟수 저장
# Qc2, Qs2 = Quick_Sort2 비교, 교환(또는 이동) 횟수 저장
Qc, Qs, Mc, Ms, Hc, Hs = 0, 0, 0, 0, 0, 0
Qc2, Qs2 = 0, 0 #quick_sort2
Qc4, Qs4 = 0, 0 # insertion_binary_search
Qc3, Qs3 = 0, 0 #quick_sort3
Mc2, Ms2 = 0, 0 #merge sort2

n = int(input())
random.seed()
A = [] # Quick Sort
for i in range(n):
    A.append(random.randint(-1000,1000))
B = A[:] # Merge Sort
C = A[:] # Heap Sort
D = A[:] # Quick_Sort2 추가점수 1 리스트 
E = A[:] # insertion_binary_sort 
F = A[:] # Quick_Sort3 추가점수 2 리스트
G = A[:] # Merge + insertion 추가점수 4리스트

print("")
print("Quick sort:")
print("time =", timeit.timeit("quick_sort(A, 0, n-1)", globals=globals(), number=1))
print("  comparisons = {:10d}, swaps = {:10d}\n".format(Qc, Qs))

print("Quick sort2:")
print("time =", timeit.timeit("quick_sort2(D, 0, n-1)", globals=globals(), number=1))
print("  comparisons = {:10d}, swaps = {:10d}\n".format(Qc2, Qs2))

print("Quick sort3:")
print("time =", timeit.timeit("quick_sort2(F, 0, n-1)", globals=globals(), number=1))
print("  comparisons = {:10d}, swaps = {:10d}\n".format(Qc3, Qs3))

print("Merge sort:")
print("time =", timeit.timeit("merge_sort(B, 0, n-1)", globals=globals(), number=1))
print("  comparisons = {:10d}, swaps = {:10d}\n".format(Mc, Ms))

print("Merge sort2:")
print("time =", timeit.timeit("merge_sort2(G, 0, n-1)", globals=globals(), number=1))
print("  comparisons = {:10d}, swaps = {:10d}\n".format(Mc2, Ms2))

print("Heap sort:")
print("time =", timeit.timeit("heap_sort(C)", globals=globals(), number=1))
print("  comparisons = {:10d}, swaps = {:10d}\n".format(Hc, Hs))

print("insertion_binary_sort:")
print("time =", timeit.timeit("insertion_binary_sort(E)", globals=globals(), number=1))
print("  comparisons = {:10d}, swaps = {:10d}\n".format(Qc4, Qs4))

# 진짜 정렬되었는지 check한다. 정렬이 되지 않았다면, assert 함수가 fail됨!
assert(check_sorted(A))
assert(check_sorted(B))
assert(check_sorted(C))
assert(check_sorted(D))
assert(check_sorted(E))
assert(check_sorted(F))
assert(check_sorted(G))