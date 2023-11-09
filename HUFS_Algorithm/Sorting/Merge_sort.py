# merge sort 추가 문제
# 왼쪽 반과 오른쪽 반으로 나누지 않고, 3등분 해서 재귀적으로 정렬한 후, merge하는 3-wqy merge sort 구현

def merge_sort1(A, first, last): #추가 점수 3/ merge sort A[first] ~ A[last]
	global Mc1,Ms1
	if first >= last: return
	middle1 = first + ((last - first) //3);
	middle2 = first + 2 * ((last - first)//3) + 1
	merge_sort1(A, first, middle1)
	merge_sort1(A, middle1+1, middle2)
	merge_sort1(A, middle2+1, last)
	B = []
	i = first
	j = middle1+1
	k = middle2+1
	while i <= middle1 and j <= middle2 and k <= last:
		if A[i] > A[j]:
			if A[j] > A[k]:
				B.append(A[k])
				k+=1
				Ms1+=1
			else:
				B.append(A[j])
				j+=1
				Ms1+=1
			Mc1+=1
		else:
			if A[i] > A[k]:
				B.append(A[k])
				k+=1
				Ms1+=1
			else:
				B.append(A[i])
				i+=1
				Ms1+=1
			Mc1+=1
		Mc1+=1

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
	for k in range(k, last+1): 
		B.append(A[k])
		Ms1 += 1

	for k in range(first, last+1): 
		A[k] = B[k-first]
	Ms1 += 1