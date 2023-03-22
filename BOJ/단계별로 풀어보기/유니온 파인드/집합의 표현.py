# 집합의 표현
# https://www.acmicpc.net/problem/1717
# 골드 5 | 시간 제한 2초 | 메모리 제한 128MB

'''
초기에 n+1개의 집합 {0}, {1}, {2}, ... , {n}이 있다.
여기에 합집합 연산과, 두 원소가 같은 집합에 포함되어 있는지를 확인하는 연산을 수행하려고 한다.
집합을 표현하는 프로그램을 작성하시오.
'''

'''
입력 조건
- 첫째 줄에 n, m이 주어진다. (1 <= n <= 1,000,000 / 1 <= m <= 100,000) 
- m은 입력으로 주어지는 연산의 개수이다.
- 다음 m개의 줄에는 각각의 연산이 주어진다.
- 합집합은 0 a b의 형태로 입력이 주어진다. 이는 a가 포함되어 있는 집합과, b가 포함되어 있는 집합을 합친다는 의미이다.
- 두 원소가 같은 집합에 포함되어 있는지를 확인하는 연산은 1 a b의 형태로 입력이 주어진다. 이는 a와 b가 같은 집합에 포함되어 있는지를 확인하는 연산이다.
- 0 <= a, b <= n / a, b는 정수, a와 b는 같을 수도 있다.

출력 조건
- 1로 시작하는 입력에 대해서 a와 b가 같은 집합에 포함되어 있으면 "YES" 또는 "yes"를, 그렇지 않다면 "NO" 또는 "no"를 한 줄에 하나씩 출력한다.
'''

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6) # 재귀 깊이 설정 주의 !!

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

n, m = map(int, input().split())
parent = [0] * (n + 1)

for i in range(1, n + 1):
    parent[i] = i

for _ in range(m):
    oper, a, b = map(int, input().split())
    if oper == 0:
        union_parent(parent, a, b)
    elif oper == 1:
        if find_parent(parent, a) == find_parent(parent, b):
            print("YES")
        else:
            print("NO")

# 메모리 77100KB | 시간 368ms | 코드 길이 715B