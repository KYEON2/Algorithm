def sorted_matrix(matrix, target):
	n=len(matrix)
	row, col = 0, n-1 #시작 위치를 오른쪽 맨 위로 설정
	
	while row < n and col >= 0:
		if matrix[row][col] == target:
			return (row,col) #찾았을 때 해당 인덱스 반환
		elif matrix[row][col]>target:
			col -= 1 #현재값이 더 크면 왼쪽으로 이동
		else:
			row+= 1 #현재값이 작으면 아래로 이동
			
	return (-1, -1) #찾지 못한경우 

#n 번의 행과 열의 값을 비교하면서 시간복잡도는 O(n)이다


n, k = map(int,input().split())
matrix = []
for _ in range(n):
	row = list(map(int, input().split()))
	matrix.append(row)
	
result = sorted_matrix(matrix,k) #k값 찾기
	
print(f"({result[0]}, {result[1]})")
