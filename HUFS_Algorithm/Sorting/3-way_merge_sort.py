#GPT참고
import random, timeit

def merge_sort3(A, first, last):
    if first < last:
        mid1 = first + (last - first) // 3
        mid2 = first + 2 * (last - first) // 3

        merge_sort3(A, first, mid1)
        merge_sort3(A, mid1 + 1, mid2)
        merge_sort3(A, mid2 + 1, last)

        three_way_merge(A, first, mid1, mid2, last)

def three_way_merge(A, first, mid1, mid2, last):
    L = A[first:mid1 + 1]  # 첫 번째 부분 배열
    M = A[mid1 + 1:mid2 + 1]  # 두 번째 부분 배열
    R = A[mid2 + 1:last + 1]  # 세 번째 부분 배열

    i = j = k = 0

    # 각 부분 배열에서 가장 작은 원소 선택하며 병합
    while i < len(L) or j < len(M) or k < len(R):
        min_L = L[i] if i < len(L) else float('inf')
        min_M = M[j] if j < len(M) else float('inf')
        min_R = R[k] if k < len(R) else float('inf')

        min_val = min(min_L, min_M, min_R)

        if i < len(L) and min_val == L[i]:
            A[first + i + j + k] = L[i]
            i += 1
        elif j < len(M) and min_val == M[j]:
            A[first + i + j + k] = M[j]
            j += 1
        else:
            A[first + i + j + k] = R[k]
            k += 1

    # 나머지 부분 배열 병합
    while i < len(L):
        A[first + i + j + k] = L[i]
        i += 1

    while j < len(M):
        A[first + i + j + k] = M[j]
        j += 1

    while k < len(R):
        A[first + i + j + k] = R[k]
        k += 1
# 사용 예시
arr = [12, 11, 13, 5, 6, 7, 1, 3]
merge_sort3(arr, 0, len(arr) - 1)
print("정렬된 배열:", arr)