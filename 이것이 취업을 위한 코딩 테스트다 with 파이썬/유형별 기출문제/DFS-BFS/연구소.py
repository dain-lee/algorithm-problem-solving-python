# 연구소
# 난이도 중 | 풀이 시간 40분 | 시간 제한 2초 | 메모리 제한 512MB

'''
인체에 치명적인 바이러스를 연구하던 연구소에서 바이러스가 유출되었습니다.
다행히 바이러스는 아직 퍼지지 않았고, 바이러스의 확산을 막기 위해서 연구소에 벽을 세우려고 합니다.
연구소는 크기가 N X M인 직사각형으로 나타낼 수 있으며, 직사각형은 1 X 1 크기의 정사각형으로 나누어져 있습니다.
연구소는 빈칸, 벽으로 이루어져 있으며, 벽은 칸 하나를 가득 차지합니다.
일부 칸은 바이러스가 존재하며, 이 바이러스는 상하좌우로 인접한 빈칸으로 모두 퍼져나갈 수 있습니다.
새로 세울 수 있는 벽의 개수는 3개이며, 꼭 3개를 세워야 합니다.
예를 들어, 다음과 같이 연구소가 생긴 경우를 살펴보겠습니다.

2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0

이때, 0은 빈칸, 1은 벽, 2는 바이러스가 있는 곳입니다.
아무런 벽을 세우지 않는다면, 바이러스는 모든 빈칸으로 퍼져나갈 수 있습니다.
2행 1열, 1행 2열, 4행 6열에 벽을 세운다면 지도의 모양은 다음과 같아집니다.

2 1 0 0 1 1 0
1 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 1 0
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0

바이러스가 퍼진 뒤의 모습은 다음과 같아집니다.

2 1 0 0 1 1 2
1 0 1 0 1 2 2
0 1 1 0 1 2 2
0 1 0 0 0 1 2
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0

벽을 3개 세운 뒤, 바이러스가 퍼질 수 없는 곳을 안전 영역이라고 할 때 위의 지도에서 안전 영역의 크기는 27입니다.
연구소의 지도가 주어졌을 때 얻을 수 있는 안전 영역 크기의 최댓값을 구하는 프로그램을 작성하세요.
'''

'''
입력 조건
- 첫째 줄에 지도의 세로 크기 N과 가로 크기 M이 주어집니다. (3 <= N, M <= 8)
- 둘째 줄부터 N개의 줄에 지도의 모양이 주어집니다. 0은 빈칸, 1은 벽, 2는 바이러스가 있는 위치입니다. 2의 개수는 2보다 크거나 같고, 10보다 작거나 같은 자연수입니다.
- 빈칸의 개수는 3개 이상입니다.

출력 조건
- 첫째 줄에 얻을 수 있는 안전 영역의 최대 크기를 출력합니다.
'''

'''
벽을 3개 설치하는 모든 경우의 수를 다 계산해야 함
전체 맵의 크기가 8x8 이므로, 벽을 설치할 수 있는 모든 조합의 수는 최악의 경우(바이러스가 하나도 존재하지 않는 경우) 64C3이 될 것
이는 100,000보다도 작은 수이므로, 모든 경우의 수를 고려해도 제한 시간 안에 문제를 해결할 수 있음
모든 조합을 계산할 때는 파이썬의 조합 라이브러리를 이용하거나, DFS 혹은 BFS를 이용하여 해결할 수 있음
따라서 벽의 개수가 3개가 되는 모든 조합을 찾은 뒤에 그러한 조합에 대해서 안전 영역의 크기를 계산
'''

import copy
from collections import deque

n, m = map(int, input().split())
graph = []
locations = [] # 벽을 설치할 수 있는 좌표들

for i in range(n): # 연구소 지도 입력 받기
    data = list(map(int, input().split()))
    graph.append(data)
    for j in range(m): # 빈칸(0)이면 죄표를 locations 배열에 저장
        if data[j] == 0:
            locations.append((i, j))

dx = [-1, 1, 0, 0] # 상하좌우
dy = [0, 0, -1, 1]

def bfs(graph): # 벽을 설치한 후 바이러스가 퍼지는 것을 bfs로 계산
    queue = deque()
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 2: # 바이러스가 있으면 좌표를 초기 큐에 삽입
                queue.append((i, j))

    while queue:
        x, y = queue.popleft()
        for i in range(4): # 상하좌우
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 0: # 빈칸이면 바이러스를 퍼뜨림
                graph[nx][ny] = 2
                queue.append((nx, ny))

result = 0

for i in range(len(locations)):
    for j in range(i + 1, len(locations)):
        for k in range(j + 1, len(locations)):
            temp_graph = copy.deepcopy(graph) # 임시 배열 복사
            # 벽을 설치할 수 있는 좌표들 중 3개를 선택
            temp_graph[locations[i][0]][locations[i][1]] = 1
            temp_graph[locations[j][0]][locations[j][1]] = 1
            temp_graph[locations[k][0]][locations[k][1]] = 1

            bfs(temp_graph) # 벽을 설치한 후 바이러스를 퍼뜨림
            temp = 0
            for a in temp_graph:
                for b in a:
                    if b == 0: # 바이러스를 퍼뜨린 후에도 빈칸이면 안전 영역
                        temp += 1
            if temp > result: # 안전 영역 크기의 최댓값 구하기
                result = temp

print(result)