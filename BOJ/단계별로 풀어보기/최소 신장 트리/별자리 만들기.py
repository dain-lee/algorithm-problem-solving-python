# 별자리 만들기
# https://www.acmicpc.net/problem/4386
# 골드 3 | 시간 제한 1초 | 메모리 제한 128MB

'''
도현이는 우주의 신이다.
이제 도현이는 아무렇게나 널브러져 있는 n개의 별들을 이어서 별자리를 하나 만들 것이다.
별자리의 조건은 다음과 같다.

- 별자리를 이루는 선은 서로 다른 두 별을 일직선으로 이은 형태이다.
- 모든 별들은 별자리 위의 선을 통해 서로 직/간접적으로 이어져 있어야 한다.

별들이 2차원 평면 위에 놓여 있다.
선을 하나 이을 때마다 두 별 사이의 거리만큼의 비용이 든다고 할 때, 별자리를 만드는 최소 비용을 구하시오.
'''

'''
입력 조건
- 첫째 줄에 별의 개수 n이 주어진다. (1 ≤ n ≤ 100)
- 둘째 줄부터 n개의 줄에 걸쳐 각 별의 x, y좌표가 실수 형태로 주어지며, 최대 소수점 둘째자리까지 주어진다.
- 좌표는 1000을 넘지 않는 양의 실수이다.

출력 조건
- 첫째 줄에 정답을 출력한다. 절대/상대 오차는 10^-2까지 허용한다.
'''

import math

def find_parent(parent, x):
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

n = int(input())
parent = [0] * n

for i in range(n):
    parent[i] = i

stars = []
dist = []
result = 0

for _ in range(n):
    x, y = map(float, input().split())
    stars.append((x, y))

for i in range(n): # 모든 별 사이의 거리 구하기
    for j in range(1, n-i):
        x1, y1 = stars[i]
        x2, y2 = stars[i+j]
        # (거리, 인덱스1, 인덱스2) 저장
        # 소수점 둘째 자리 까지만
        dist.append((round(math.sqrt(pow(x1-x2,2) + pow(y1-y2,2)), 2), i, i+j))

dist.sort() # 거리가 짧은 순서대로 

for d in dist:
    cost, a, b = d
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)

# 메모리 33376KB | 시간 56ms | 코드 길이 848B