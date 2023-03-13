'''
서로소 집합 - 공통 원소가 없는 두 집합
서로소 집합 자료구조는 2개의 원소가 포함된 집합을 하나의 집합으로 합치는 union(합집합) 연산과,
특정한 원소가 속한 집합이 어떤 집합인지 알려주는 find(찾기) 연산으로 조작

서로소 집합 알고리즘 (union-find)
1. union(합집합) 연산을 확인하여, 서로 연결된 두 노드 A, B를 확인한다.
    a. A와 B의 루트 노트 A', B'를 각각 찾는다.
    b. A'와 B' 중에서 더 번호가 작은 원소를 부모 노드로 설정한다.
2. 모든 union(합집합) 연산을 처리할 때까지 1번 과정을 반복한다.

find 연산을 경로 압축을 적용하여 최적화 - 해당 노드가 루트 노드가 아니면, 부모 테이블에 저장되어 있는 부모 노드를 루트 노드로 변경

노드의 개수가 1,000개이고, union 및 find 연산이 총 100만 번 수행될 때, 약 1,000만 번 가량의 연산이 필요
'''

# 서로소 집합 알고리즘

# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수와 간선(union 연산)의 개수 입력받기
v, e = map(int, input().split())
parent = [0] * (v + 1) # 부모 테이블 초기화

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

# union 연산을 각각 수행
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

# 각 원소가 속한 집합 출력
print('각 원소가 속한 집합: ', end='')
for i in range(1, v + 1):
    print(find_parent(parent, i), end=' ')

print()

# 부모 테이블 내용 출력
print('부모 테이블: ', end='')
for i in range(1, v + 1):
    print(parent[i], end=' ')



'''
서로소 집합은 무방향 그래프 내에서의 사이클을 판별할 때 사용할 수 있음
(방향 그래프에서의 사이클 여부는 DFS를 이용하여 판별)

1. 각 간선을 확인하며 두 노드의 루트 노드를 확인
    a. 루트 노드가 서로 다르다면 두 노드에 대하여 union 연산 수행
    b. 루트 노드가 서로 같다면 사이클(Cycle)이 발생
2. 그래프에 포함되어 있는 모든 간선에 대하여 1번 과정을 반복
'''

# 서로소 집합을 활용한 사이클 판별

# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수와 간선(union 연산)의 개수 입력받기
v, e = map(int, input().split())
parent = [0] * (v + 1) # 부모 테이블 초기화

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

cycle = False # 사이클 발생 여부

for i in range(e):
    a, b = map(int, input().split())
    # 사이클이 발생한 경우 종료
    if find_parent(parent, a) == find_parent(parent, b):
        cycle = True
        break
    # 사이클이 발생하지 않았다면 합집합(union) 수행
    else:
        union_parent(parent, a, b)

if cycle:
    print("사이클이 발생했습니다.")
else:
    print("사이클이 발생하지 않았습니다.")