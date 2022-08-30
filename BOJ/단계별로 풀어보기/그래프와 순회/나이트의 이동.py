# 나이트의 이동
# https://www.acmicpc.net/problem/7562
# 실버 1 | 시간 제한 1초 | 메모리 제한 256MB

'''
체스판 위에 한 나이트가 놓여져 있다.
나이트가 한 번에 이동할 수 있는 칸은 아래 그림에 나와있다.
나이트가 이동하려고 하는 칸이 주어진다.
나이트는 몇 번 움직이면 이 칸으로 이동할 수 있을까?
'''

'''
입력 조건
- 입력의 첫째 줄에는 테스트 케이스의 개수가 주어진다.
- 각 테스트 케이스는 세 줄로 이루어져 있다.
- 첫째 줄에는 체스판의 한 변의 길이 l(4 ≤ l ≤ 300)이 주어진다.
- 체스판의 크기는 l × l이다. 체스판의 각 칸은 두 수의 쌍 {0, ..., l-1} × {0, ..., l-1}로 나타낼 수 있다.
- 둘째 줄과 셋째 줄에는 나이트가 현재 있는 칸, 나이트가 이동하려고 하는 칸이 주어진다.

출력 조건
- 각 테스트 케이스마다 나이트가 최소 몇 번만에 이동할 수 있는지 출력한다.
'''

from collections import deque
import sys
input = sys.stdin.readline

n = int(input())

dx = [-2, -1, 1, 2, 2, 1, -1, -2] # 나이트가 갈 수 있는 8가지 방향 정의
dy = [1, 2, 2, 1, -1, -2, -2, -1]

def bfs(x, y):
        global resultx, resulty
        queue = deque([(x, y)])
        while queue:
            x, y = queue.popleft()
            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx <= -1 or nx >= l or ny <= -1 or ny >= l:
                    continue
                if graph[nx][ny] != 0: # 방문 했던 위치이면 넘어감
                    continue
                graph[nx][ny] = graph[x][y] + 1 # 이동한 위치 = 현재 위치 + 1
                if nx == end_x and ny == end_y: # 이동한 위치가 나이트가 이동하려고 하는 마지막 칸이면
                    return graph[nx][ny]
                queue.append((nx, ny))

for _ in range(n):
    l = int(input())
    graph = [[0] * l for _ in range(l)]

    start_x, start_y = map(int, input().split())
    end_x, end_y = map(int, input().split())

    if start_x == end_x and start_y == end_y: # 시작 칸과 마지막 칸 위치가 같으면
        print(0)
        continue

    print(bfs(start_x, start_y))

# 메모리 32436KB | 시간 2372ms | 코드 길이 1002B