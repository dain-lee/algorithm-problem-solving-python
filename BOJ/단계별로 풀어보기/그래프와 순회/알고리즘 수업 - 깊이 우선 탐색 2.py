# 알고리즘 수업 - 깊이 우선 탐색 2
# https://www.acmicpc.net/problem/24480
# 실버 2 | 시간 제한 1초 | 메모리 제한 512MB

'''
오늘도 서준이는 깊이 우선 탐색(DFS) 수업 조교를 하고 있다.
아빠가 수업한 내용을 학생들이 잘 이해했는지 문제를 통해서 확인해보자.
N개의 정점과 M개의 간선으로 구성된 무방향 그래프(undirected graph)가 주어진다.
정점 번호는 1번부터 N번이고 모든 간선의 가중치는 1이다.
정점 R에서 시작하여 깊이 우선 탐색으로 노드를 방문할 경우 노드의 방문 순서를 출력하자.
깊이 우선 탐색 의사 코드는 다음과 같다.
인접 정점은 내림차순으로 방문한다.

dfs(V, E, R) {  # V : 정점 집합, E : 간선 집합, R : 시작 정점
    visited[R] <- YES;  # 시작 정점 R을 방문 했다고 표시한다.
    for each x ∈ E(R)  # E(R) : 정점 R의 인접 정점 집합.(정점 번호를 내림차순으로 방문한다)
        if (visited[x] = NO) then dfs(V, E, x);
}
'''

'''
입력 조건
- 첫째 줄에 정점의 수 N (5 ≤ N ≤ 100,000), 간선의 수 M (1 ≤ M ≤ 200,000), 시작 정점 R (1 ≤ R ≤ N)이 주어진다.
- 다음 M개 줄에 간선 정보 u v가 주어지며 정점 u와 정점 v의 가중치 1인 양방향 간선을 나타낸다. (1 ≤ u < v ≤ N, u ≠ v)
- 모든 간선의 (u, v) 쌍의 값은 서로 다르다.

출력 조건
- 첫째 줄부터 N개의 줄에 정수를 한 개씩 출력한다.
- i번째 줄에는 정점 i의 방문 순서를 출력한다.
- 시작 정점의 방문 순서는 1이다.
- 시작 정점에서 방문할 수 없는 경우 0을 출력한다.
'''

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6) # 재귀 허용 깊이를 수동으로 늘림

n, m, r = map(int, input().split())
graph = [[] for _ in range(n + 1)] # 빈 그래프 생성
visited = [0] * (n + 1) # 방문 순서 리스트
count = 1 # 방문 순서

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v) # 양방향 간선이므로 둘 다 입력
    graph[v].append(u)

for i in graph:
    i.sort(reverse=True) # 내림차순으로 정렬

def dfs(graph, v, visited):
    global count
    visited[v] = count # 방문 순서 저장
    for i in graph[v]:
        if visited[i] == 0:
            count += 1
            dfs(graph, i, visited)

dfs(graph, r, visited)

for i in visited[1:]:
    print(i)

# 메모리 161048KB | 시간 652ms | 코드 길이 555B