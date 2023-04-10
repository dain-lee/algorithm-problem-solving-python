# 특정 거리의 도시 찾기
# 난이도 중하 | 풀이 시간 30분 | 시간 제한 2초 | 메모리 제한 256MB

'''
어떤 나라에는 1 ~ N번까지의 도시와 M개의 단방향 도로가 존재합니다.
모든 도로의 거리는 1입니다.
이때 특정한 도시 X로부터 출발하여 도달할 수 있는 모든 도시 중에서, 최단 거리가 정확히 K인 모든 도시의 번호를 출력하는 프로그램을 작성하세요.
또한 출발 도시 X에서 출발 도시 X로 가는 최단 거리는 항상 0이라고 가정합니다.
'''

'''
입력 조건
- 첫째 줄에 도시의 개수 N, 도로의 개수 M, 거리 정보 K, 출발 도시의 번호 X가 주어집니다. (2 <= N <= 300,000, 1 <= M <= 1,000,000, 1 <= K <= 300,000, 1 <= X <= N)
- 둘째 줄부터 M개의 줄에 걸쳐서 두 개의 자연수 A, B가 주어지며, 각 자연수는 공백으로 구분합니다. 이는 A번 도시에서 B번 도시로 이동하는 단방향 도로가 존재한다는 의미입니다. (1 <= A, B <= N)
- 단, A와 B는 서로 다른 자연수입니다.

출력 조건
- X로부터 출발하여 도달할 수 있는 도시 중에서, 최단 거리가 K인 모든 도시의 번호를 한 줄에 하나씩 오름차순으로 출력합니다.
- 이때 도달할 수 있는 도시 중에서, 최단 거리가 K인 도시가 하나도 존재하지 않으면 -1을 출력합니다.
'''

from collections import deque

def bfs(x):
    queue = deque([x])
    
    while queue:
        now = queue.popleft()
        for i in graph[now]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = visited[now] + 1

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

bfs(x) # bfs로 각 도시까지의 최단 거리 찾기
visited[x] = 0

found = False
for i in range(1, n + 1):
    if visited[i] == k:
        print(i)
        found = True

if not found: # 최단 거리가 K인 도시가 없으면, -1 출력
    print(-1)