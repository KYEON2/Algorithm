def search(building):
	building.append(0)
	stack = []
	max_area = 0
	
	for i, h in enumerate(building): 
     #enumerate -> 파이썬에서 반복 가능한 객체를 반복할 때, 각 항목의 인덱스와 값을 함께 얻기 위해 사용하는 함수
     # -> 루프를 실행하면서 각 항목의 인덱스와 그에 해당하는 값을 동시에 얻을 수 있음
		while stack and building[stack[-1]] > h:
			height = building[stack.pop()]
			width = i if not stack else i - stack[-1] -1
			max_area = max(max_area, width * height)
		stack.append(i)
		
	return max_area

n = int(input())
building = list(map(int, input().split()))
print(search(building))




# 높이가 증가하는 순서로 스택에 저장하여 스택의 맨 위에 가장 높은 빌딩 위치
# 현재 빌딩의 높이가 스택의 맨 위 빌딩보다 크거나 같으면 스택에 현재 빌딩의 인덱스를 추가
# 현재 빌딩의 높이가 스택의 맨 위 빌딩보다 낮으면 이전 빌딩에서 최대 직사각형을 계산
# 직사각형의 넓이는 현재 빌딩의 인덱스에서 스택의 두번째 요소의 인덱스를 뺀 값
# 직사각형의 높이는 스택의 맨 위 빌딩의 높이
# 계산한 직사각형의 면직이 현재까지의 최대 면적보다 크면 최대 면적을 업데이트 한다.

# 수행시간 O(n) 
# n은 빌딩의 수로, 실행 시간은 입력으로 주어진 빌딩 수에 비례하며 일반적으로 빌딩 수가 많을수록 실행 시간이 더 오래 걸림
