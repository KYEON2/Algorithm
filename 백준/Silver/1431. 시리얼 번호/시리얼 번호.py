#lambda 함수 익히기
#arr.sort(key = lambda x : (정렬기준1, 정렬기준2, 정렬기준3, …)) -> sort 함수에는 key 파라미터를 통해 정렬의 기준이 되는 값을 지정해줄 수 있음

#lambda식을 이용하면 한 번에 여러 개의 값을 지정해줄 수 있음

n = int(input())

def sum_num(inputs):
    result = 0
    for i in inputs:
        if i.isdigit():
            result+=int(i)
    return result

arr = []
for i in range(n):
    a = input()
    arr.append(a)

arr.sort(key = lambda x:(len(x), sum_num(x), x)) #람다 함수 -> 이름이 없는 함수
for i in arr:
    print(i)
    