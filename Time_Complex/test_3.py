import time, random

def evaluate_n2(A, x):
	# code for O(n^2)-time function
	global t1_start, t1_end
	t1_start = time.process_time()
	result_1 = 0
	for i in range(n):
		total_x = 1
		for j in range(i):
			total_x *= x
		result_1 += A[i]*total_x
	t1_end = time.process_time()
	
	
def evaluate_n(A, x):
	# code for O(n)-time function
	global t2_start, t2_end
	t2_start = time.process_time()
	total_x = 1
	result_2 = 0
	for i in range(n):
		result_2 += A[i] * total_x
		total_x *= x
	t2_end = time.process_time()
	
	
random.seed()		# random 함수 초기화
# n 입력받음
n = int(input())

# 리스트 A를 randint를 호출하여 n개의 랜덤한 숫자로 채움
A = []
for i in range (n):
	A.append(random.randint(-1000,1000))
	
x = random.randint(-1000,1000)
	
# evaluate_n2 호출
evaluate_n2(A,x)

# evaluate_n 호출
evaluate_n(A, x)

# 두 함수의 수행시간 출력
print(f'evaluate_n2: {t1_end - t1_start:.10f}')
print(f'evaluate_n: {t2_end - t2_start:.10f}')