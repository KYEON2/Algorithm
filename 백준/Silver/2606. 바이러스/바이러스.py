import sys
input = sys.stdin.readline

n = int(input())  # 컴퓨터의 수
m = int(input())  # 연결의 수

sets = []  # 모든 집합을 저장할 리스트
index_map = {}  # 각 컴퓨터가 속한 집합의 인덱스를 저장

for _ in range(m):
    p, q = map(int, input().strip().split())
    set_found = False
    new_set = set([p, q])

    # p와 q가 이미 포함된 집합을 찾아 병합한다.
    to_merge = []
    for idx, s in enumerate(sets):
        if p in s or q in s:
            to_merge.append(idx)

    # 병합할 집합들을 하나의 집합으로 합친다.
    for idx in reversed(to_merge):  # 리스트의 뒤에서부터 제거하여 인덱스 오류 방지
        new_set.update(sets[idx])
        sets.pop(idx)
    
    # 병합된 새 집합을 추가
    sets.append(new_set)
    
    # 새로운 집합 인덱스 업데이트
    for item in new_set:
        index_map[item] = len(sets) - 1

# 1번 컴퓨터가 감염시킬 수 있는 컴퓨터의 수를 계산 (1번을 제외한 나머지)
count = 0
for s in sets:
    if 1 in s:
        count = len(s) - 1
        break

print(count)
