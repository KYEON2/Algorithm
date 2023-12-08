#최장 증가 부수열 문제 DP 알고리즘 1 -> 시간복잡도 O(nlogn)

def binary_search(target,lis):
    start,end = 0,len(lis)-1 # 초기 시작점과 끝점
    while start < end:
        mid = (start + end) // 2 # 중간값

        if lis[mid] == target: # 중간값이 타겟과 같다면 중간값의 위치를 반환
            return mid

        # 타겟보다 큰 값 중 가장 작은 값의 위치는 
        # 아래와 같이 바로 전 값보다 크면서 바로 현재 값(중앙)보단 작은 위치이다
        elif lis[mid-1] < target < lis[mid]: 
            return mid

        # target이 더 작으면 왼쪽 더 탐색
        elif target < lis[mid]:
            end = mid - 1

        # target이 더 크면 오른쪽 더 탐색
        else:
            start = mid + 1

    return start # 만약 시작점과 끝점이 같다면 시작점을 반환

def sol():
    n = int(input())
    a = list(map(int,input().split()))
    lis = [a[0]] # A 수열의 첫번째 값
    # A 수열의 두번째 값부터 LIS의 마지막 값과 비교
    for i in range(1,n):
        target = a[i]
        if lis[-1] < target: # 타겟이 더 크다면 LIS 에 추가
            lis.append(target)
        else:                # 타겟이 더 작다면 이분탐색을 통해 LIS 갱신
            idx = binary_search(target,lis)
            lis[idx] = target

    return len(lis) # 최종 LIS 길이 반환

print(sol())





"""
lis 리스트에 증가하는 부분 수열을 담으려고 한다.
주어진 A 수열의 첫 번째 값을 lis에 담은 상태로 초기화를 하고 시작한다.
A 수열의 두 번째 값(target)부터 마지막 target까지를 lis의 맨 마지막 값과 비교하여
target이 더 크다면 lis에 target을 추가하고,
target이 더 작다면 이분탐색을 통해 lis 값 중 target보다 크면서 제일 작은 값을 target으로 갱신한다.
"""