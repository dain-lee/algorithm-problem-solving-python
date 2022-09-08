# 이분 그래프
# https://www.acmicpc.net/problem/1707
# 골드 4 | 시간 제한 2초 | 메모리 제한 256MB

'''
그래프의 정점의 집합을 둘로 분할하여, 각 집합에 속한 정점끼리는 서로 인접하지 않도록 분할할 수 있을 때, 그러한 그래프를 특별히 이분 그래프 (Bipartite Graph) 라 부른다.
그래프가 입력으로 주어졌을 때, 이 그래프가 이분 그래프인지 아닌지 판별하는 프로그램을 작성하시오.
'''

'''
입력 조건
- 입력은 여러 개의 테스트 케이스로 구성되어 있는데, 첫째 줄에 테스트 케이스의 개수 K가 주어진다.
- 각 테스트 케이스의 첫째 줄에는 그래프의 정점의 개수 V와 간선의 개수 E가 빈 칸을 사이에 두고 순서대로 주어진다.
- 각 정점에는 1부터 V까지 차례로 번호가 붙어 있다.
- 이어서 둘째 줄부터 E개의 줄에 걸쳐 간선에 대한 정보가 주어지는데, 각 줄에 인접한 두 정점의 번호 u, v (u ≠ v)가 빈 칸을 사이에 두고 주어진다.

출력 조건
- K개의 줄에 걸쳐 입력으로 주어진 그래프가 이분 그래프이면 YES, 아니면 NO를 순서대로 출력한다.
'''

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(v, group):
    visited[v] = group # 1 또는 -1
    for i in graph[v]:
        if visited[i] == 0: # 인접 정점이 방문하지 않은 정점일때
            if not dfs(i, -group): # 다른 그룹으로 dfs한 결과가 false이면
                return False
        elif visited[i] == group: # 인접 정점이 같은 그룹이면 이분 그래프가 아님
            return False
    return True

k = int(input())
for _ in range(k):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v + 1)]
    visited = [0] * (v + 1)

    for _ in range(e):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    bipartite = True # 이분 그래프 여부
    for i in range(1, v + 1): # 비연결 정점까지 방문해야 함
        if visited[i] != 0: # 이미 방문한 정점이면 continue
            continue
        if not bipartite: # 이분 그래프면 break
            break
        bipartite = dfs(i, 1)

    if bipartite:
        print("YES")
    else:
        print("NO")