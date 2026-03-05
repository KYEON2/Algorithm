rows, cols = map(int, input().split())

matrix1 = [list(map(int, input().split())) for _ in range(rows)]
matrix2 = [list(map(int, input().split())) for _ in range(rows)]

result = []
for i in range(rows):
    row_sum = []
    for j in range(cols):
        row_sum.append(matrix1[i][j] + matrix2[i][j])
    result.append(row_sum)


for r in result:
    print(*r)