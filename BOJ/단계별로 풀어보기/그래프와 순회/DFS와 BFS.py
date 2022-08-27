# DFS와 BFS
# https://www.acmicpc.net/problem/1260
# 실버 2 | 시간 제한 2초 | 메모리 제한 128MB

'''
그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오.
단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다.
정점 번호는 1번부터 N번까지이다.
'''

'''
입력 조건
- 첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다.
- 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다.
- 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다.
- 입력으로 주어지는 간선은 양방향이다.

출력 조건
- 첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다.
- V부터 방문된 점을 순서대로 출력하면 된다.
'''

from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6) # 재귀 허용 깊이를 수동으로 늘림

n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited_d = [False] * (n + 1) # dfs 방문 여부
visited_b = [False] * (n + 1) # bfs 방문 여부

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort() # 오름차순으로 정렬

def dfs(graph, v, visited_d):
    visited_d[v] = True
    print(v, end=' ') # dfs를 하면서 방문한 노드 출력
    for i in graph[v]:
        if not visited_d[i]:
            dfs(graph, i, visited_d)

def bfs(graph, start, visited_b):
    queue = deque([start])
    visited_b[start] = count
    while queue:
        v = queue.popleft()
        print(v, end=' ') # bfs를 하면서 방문한 노드 출력
        for i in graph[v]:
            if not visited_b[i]:
                queue.append(i)
                visited_b[i] = True

dfs(graph, v, visited_d)
count = 1
print()
bfs(graph, v, visited_b)

# 메모리 32468KB | 시간 100ms | 코드 길이 886B