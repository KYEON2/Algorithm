#4분면 이용해서 k찾기

# 강의노트에 적힌 대로 구간을 정해줘서 가운데 중앙값 x와 y를 지정한다.
# 중앙값을 기준으로 몇사분면에서 탐색을 할지 재귀 탐색 코드를 작성하여 재귀를 돌려서 구간을 정하고 
# 첫번째 행, 열과 마지막 행, 열을 입력받아서 더 큰 4*4, 8*8행렬이 와도 2*2 행렬만 남기도록 쪼개준다.
# 2*2 행렬로 쪼개어졌다면 이제 거기서 2차원리스트의 인덱스값을 +1해주면서 비교해서 k값과 같다면 그 좌표를 반환하여 출력해준다.


# n * n 행렬이라고 단순하게 가정하면, T(n) = n * n 행렬에 대한 탐색 시간
# T(n) <= 3 * T(n/2) + c
# O(n^1.584)


def search(grid, k, mi, mj, ni, nj): # 2차원 리스트, k, 첫 행, 첫 열, 마지막 행, 마지막 열
	ki = (mi+ni) // 2 
	kj = (mj+nj) // 2 
	
	if all(k not in l for l in grid): # 만약 grid 안에 찾고자 하는 값이 없을 경우
		return -1, -1
	
	if ki == ni and kj == nj: # 2, 5, 8, 10 오류 잡음
		if grid[mi][nj] == k: 
			return mi, nj
		elif grid[ni][mj] == k: 
			return ni, mj
		else:
			return False # 이거 있고 없고로 테케 2번이 갈림


	if grid[ki][kj] == k: # 중간값 x일 때 맞으면 빙고
		#print(ki, kj)
		return ki, kj
	
	elif grid[ki+1][kj+1] == k: #중간값 y일 때 맞으면 빙고
		#print(ki, kj)
		return ki+1, kj+1
	
	elif grid[ki][kj+1] == k: #그 외 구간
		#print(ki, kj)
		return ki, kj+1
	
	elif grid[ki+1][kj] == k: # 그 외 구간
		#print(ki, kj)
		return ki+1, kj
	
	elif k < grid[ki][kj] : # D에 없음
		return search(grid, k, mi, kj+1, ki, nj) or search(grid, k, mi, mj, ki, kj) or search(grid, k, ki+1, mj, ni, kj) # A, B, C
	elif grid[ki+1][kj+1] < k: # B에 없음
		return search(grid, k, mi, kj+1, ki, nj) or search(grid, k, ki+1, mj, ni, kj) or search(grid, k, ki+1, kj+1, ni, nj) # A, C, D
	elif grid[ki][kj] < k < grid[ki+1][kj+1]: # B와 D에 없음
		return search(grid, k, mi, kj+1, ki, nj) or search(grid, k, ki+1, mj, ni, kj) # A, C

n, k = map(int, input().split()) # 첫 줄 n, k 값 입력
grid = [
	list(map(int, input().split()))
	for _ in range(n)
]
answer = search(grid, k, 0, 0, n-1, n-1) # 2차원 행렬, n, k, 첫 행, 첫 열, 마지막 행, 마지막 열
print(answer)