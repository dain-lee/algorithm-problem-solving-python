# 벽 부수고 이동하기
# https://www.acmicpc.net/problem/2206
# 골드 4 | 시간 제한 2초 | 메모리 제한 192MB

'''
N×M의 행렬로 표현되는 맵이 있다.
맵에서 0은 이동할 수 있는 곳을 나타내고, 1은 이동할 수 없는 벽이 있는 곳을 나타낸다.
당신은 (1, 1)에서 (N, M)의 위치까지 이동하려 하는데, 이때 최단 경로로 이동하려 한다.
최단경로는 맵에서 가장 적은 개수의 칸을 지나는 경로를 말하는데, 이때 시작하는 칸과 끝나는 칸도 포함해서 센다.
만약에 이동하는 도중에 한 개의 벽을 부수고 이동하는 것이 좀 더 경로가 짧아진다면, 벽을 한 개 까지 부수고 이동하여도 된다.
한 칸에서 이동할 수 있는 칸은 상하좌우로 인접한 칸이다.
맵이 주어졌을 때, 최단 경로를 구해 내는 프로그램을 작성하시오.
'''

'''
입력 조건
- 첫째 줄에 N(1 ≤ N ≤ 1,000), M(1 ≤ M ≤ 1,000)이 주어진다.
- 다음 N개의 줄에 M개의 숫자로 맵이 주어진다. (1, 1)과 (N, M)은 항상 0이라고 가정하자.

출력 조건
- 첫째 줄에 최단 거리를 출력한다. 불가능할 때는 -1을 출력한다.
'''

from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)] # visited 리스트를 3차원 그래프로 나타냄
# visited[x][y][0]은 벽을 부수지 않은 경로, visited[x][y][1]은 벽을 부순 경로
visited[0][0][0] = 1

dx = [-1, 1, 0, 0] # 상하좌우 정의
dy = [0, 0, -1, 1]

def bfs(x, y, z):
    queue = deque()
    queue.append((x, y, z))

    while queue:
        x, y, z = queue.popleft()
        if x == n - 1 and y == m - 1: # (N, M)에 도달하면 최단 거리 출력
            return visited[x][y][z]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            # 중간에 벽을 부순 경로는 그 이후의 경로부터는 벽을 지나갈 수 없으므로 벽이 아닌 곳들만 탐색
            # 중간에 벽을 부수지 않은 경로는 그 이후의 경로에서 벽을 부술 수 있는 선택권이 주어짐
            # 한 방향에서 벽을 부수더라도 다른 방향으로 이동하는 경우도 큐에 삽입하기 때문에, 벽을 부수지 않는 경로와 벽을 부수는 경우 모두 탐색

            if graph[nx][ny] == 1 and z == 0: # 이동할 곳이 벽이고, 벽을 아직 부수지 않았으면
                visited[nx][ny][1] = visited[x][y][0] + 1 # z를 1로 바꿈
                queue.append((nx, ny, 1))
            elif graph[nx][ny] == 0 and visited[nx][ny][z] == 0: # 이동할 곳이 벽이 아니고, 방문하지 않은 곳이면
                visited[nx][ny][z] = visited[x][y][z] + 1
                queue.append((nx, ny, z))
    
    return -1 # 불가능할 때는 -1 출력

print(bfs(0, 0, 0))