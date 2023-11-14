import random, timeit

##
## 여기에 세 가지 정렬함수를 위한 코드를...
##

# Quick sort
def quick_sort(A, first, last):
	
	global Qc, Qs
	
	if first >= last: return
	left, right = first + 1, last
	pivot = A[first]
	while left <= right:
		while left <= last and A[left] < pivot:
			left += 1
			Qc += 1
		while right > first and A[right] > pivot:
			right -= 1
			Qc += 1
		if left <= right:
			A[left], A[right] = A[right], A[left]
			Qs += 1
			left += 1
			right -= 1
	A[first], A[right] = A[right], A[first]
	Qs += 1
	
	quick_sort(A, first, right -1)
	quick_sort(A,right + 1, last)
	
	
# Merge sort
def merge_sort(A, first, last):
	
	global Ms
	
	if first >= last : return
	merge_sort(A, first, (first+last)//2)
	merge_sort(A, (first+last)//2+1, last)
	merge_two_sorted_lists(A, first, last)
	
def merge_two_sorted_lists(A, first, last):
	
	global Mc, Ms
	
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
		Ms += 1
	for k in range(j, last+1):
		B.append(A[k])
		Ms += 1
	for i in range(first, last+1):
		A[i] = B[i-first]
		Ms += 1


# Heap
def heapify(A, k, n):
	
	global Hc, Hs
	
	if n == 0:
		return None
	while 2*k+1 < n:
		L, R = 2*k+1, 2*k+2
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
			A[k], A[m] = A[m], A[k]
			k = m
			Hs += 1
		else:
			break
	
def makeHeap(A):
	n = len(A)
	for k in range(n//2-1, -1, -1):
		heapify(A, k, n)
	
def heap_sort(A):
		
	global Hc, Hs
		
	n=len(A)
	makeHeap(A)
		
	for i in range(n-1, -1, -1):
		A[0], A[i] = A[i], A[0]
		Hs += 1
		n -= 1
		heapify(A, 0, n)
		
		

def insertion_sort1(A, first, last):
	global Qc2, Qs2
	for i in range(first+1, last+1):
		Qc2 += 1
		j = i-1
		while A[j+1] < A[j] and j >= first:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1
			Qs2 += 1

def insertion_sort2(A, first, last):
	global Qc3, Qs3
	for i in range(first+1, last+1):
		Qc3 +=1
		j = i-1
		while A[j+1] < A[j] and j >= first:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1
			Qs3 += 1
	
	
# 추가점수 1 - Quick Sort
#퀵소트에 비해 비교 및 스왑 횟수가 적기 때문에 작은 배열의 경우 삽입 정렬이 퀵 정렬보다 효율적
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
	



# 추가점수 2 - Quick Sort
# 적당한 k개의 범위가 주어지지 않았기 때문에 10부터 40으로 범위를 잡고 k개로 분할한 후 , insertion sort를 사용하여 정렬하는 방법을 구현
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

	

# 추가점수 3 - Merge Sort
def merge_sort1(A, first, last):
	global Mc1, Ms1
	if first >= last: return
	middle1 = first + ((last - first)//3) 
	middle2 = first + 2*((last - first)//3) + 1
	merge_sort1(A, first, middle1)
	merge_sort1(A, middle1+1, middle2)
	merge_sort1(A, middle2+1, last)
	B = []
	i = first
	j = middle1 + 1
	k = middle2 + 1
	while i <= middle1 and j <= middle2 and k <= last:
		if A[i] > A[j]:
			if A[j] > A[k]:
				B.append(A[k])
				k += 1
				Ms1 += 1
			else:
				B.append(A[j])
				j += 1
				Ms1 += 1
			Mc1 += 1
		else:
			if A[i] > A[k]:
				B.append(A[k])
				k += 1
				Ms1 += 1
			else:
				B.append(A[i])
				i += 1
				Ms1 += 1
			Mc1 += 1
		Mc1 += 1
		
	while i <= middle1 and j <= middle2:
		if A[i] <= A[j]:
			B.append(A[i])
			Ms1 += 1
			i += 1
		else:
			B.append(A[j])
			Ms1 += 1
			j += 1
		Mc1 += 1
	
	while i <= middle1 and k <= last:
		if A[i] <= A[k]:
			B.append(A[i])
			Ms1 += 1
			i += 1
		else:
			B.append(A[k])
			Ms1 += 1
			k += 1
		Mc1 += 1
		
	while j <= middle2 and k <= last:
		if A[j] <= A[k]:
			B.append(A[j])
			Ms1 += 1
			j += 1
		else:
			B.append(A[k])
			Ms1 += 1
			k += 1
		Mc1 += 1
		
	for i in range(i, middle1+1):
		B.append(A[i])
		Ms1 += 1
	for j in range(j, middle2+1):
		B.append(A[j])
		Ms1 += 1
	for k in range(k, last +1):
		B.append(A[k])
		Ms1 += 1
		
	for k in range(first, last+1):
		A[k] = B[k-first]
	Ms1 += 1
	
	


def insertion_sort3(A, first, n): #Tim sort 를 위한 insertion_sort3 함수
	global Mc2, Ms2
	for k in range(first + 1, n + 1):
		val = A[i]
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
	merge_sort(A, first, (first+last)//2)
	merge_sort(A, (first+last)//2+1, last)
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
	

# 정렬 여부를 검사하는 check_sorted함수는 바꾸지 말 것!
# 직접 실행해보면, 어떤 값이 출력되는지 알 수 있음
# 그 외 코드는 자유롭게 수정해도 됩니다.

def check_sorted(A):
	for i in range(n-1):
		if A[i] > A[i+1]: return False
	return True

#
# Qc는 quick sort에서 리스트의 두 수를 비교한 횟수 저장
# Qs는 quick sort에서 두 수를 교환(swap)한 횟수 저장
# Mc, Ms는 merge sort에서 비교, 교환(또는 이동) 횟수 저장
# Hc, Hs는 heap sort에서 비교, 교환(또는 이동) 횟수 저장
#
Qc, Qs, Mc, Ms, Hc, Hs = 0, 0, 0, 0, 0, 0
Qc2, Qs2 = 0, 0 #quick_sort2
Qc3, Qs3 = 0, 0 #quick_sort3
Mc1, Ms1 = 0, 0 #merge_sort1
Mc2, Ms2 = 0, 0 #Tim_sort


n = int(input())
random.seed()
A = []
for i in range(n):
    A.append(random.randint(-1000,1000))
B = A[:]
C = A[:]
D = A[:] # Quick_Sort2 추가점수 1
E = A[:] # Quick_Sort3 추가점수 2
F = A[:] # Merge sort 추가점수 3
G = A[:] # Tim sort 추가점수 4


print("")
print("Quick sort:")
print("time =", timeit.timeit("quick_sort(A, 0, n-1)", globals=globals(), number=1))
print("  comparisons = {:10d}, swaps = {:10d}\n".format(Qc, Qs))

print("Quick sort2:")
print("time =", timeit.timeit("quick_sort2(D, 0, n-1)", globals=globals(), number=1))
print("  comparisons = {:10d}, swaps = {:10d}\n".format(Qc2, Qs2))

print("Quick sort3:")
print("time =", timeit.timeit("quick_sort3(E, 0, n-1)", globals=globals(), number=1))
print("  comparisons = {:10d}, swaps = {:10d}\n".format(Qc3, Qs3))

print("Merge sort:")
print("time =", timeit.timeit("merge_sort(B, 0, n-1)", globals=globals(), number=1))
print("  comparisons = {:10d}, swaps = {:10d}\n".format(Mc, Ms))

print("Merge sort1:")
print("time =", timeit.timeit("merge_sort1(F, 0, n-1)", globals=globals(), number=1))
print("  comparisons = {:10d}, swaps = {:10d}\n".format(Mc1, Ms1))

print("Heap sort:")
print("time =", timeit.timeit("heap_sort(C)", globals=globals(), number=1))
print("  comparisons = {:10d}, swaps = {:10d}\n".format(Hc, Hs))

print("Tim sort:")
print("time =", timeit.timeit("merge_sort2(G, 0, n-1)", globals=globals(), number=1))
print("  comparisons = {:10d}, swaps = {:10d}\n".format(Mc2, Ms2))

# 진짜 정렬되었는지 check한다. 정렬이 되지 않았다면, assert 함수가 fail됨!
assert(check_sorted(A))
assert(check_sorted(B))
assert(check_sorted(C))
assert(check_sorted(D))
assert(check_sorted(E))
assert(check_sorted(F))
assert(check_sorted(F))
assert(check_sorted(G))
