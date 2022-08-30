# 단지번호붙이기
# https://www.acmicpc.net/problem/2667
# 실버 1 | 시간 제한 1초 | 메모리 제한 128MB

'''
<그림 1>과 같이 정사각형 모양의 지도가 있다.
1은 집이 있는 곳을, 0은 집이 없는 곳을 나타낸다.
철수는 이 지도를 가지고 연결된 집의 모임인 단지를 정의하고, 단지에 번호를 붙이려 한다.
여기서 연결되었다는 것은 어떤 집이 좌우, 혹은 아래위로 다른 집이 있는 경우를 말한다.
대각선상에 집이 있는 경우는 연결된 것이 아니다.
<그림 2>는 <그림 1>을 단지별로 번호를 붙인 것이다.
지도를 입력하여 단지수를 출력하고, 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력하는 프로그램을 작성하시오.
'''

'''
입력 조건
- 첫 번째 줄에는 지도의 크기 N(정사각형이므로 가로와 세로의 크기는 같으며 5≤N≤25)이 입력되고, 그 다음 N줄에는 각각 N개의 자료(0혹은 1)가 입력된다.

출력 조건
- 첫 번째 줄에는 총 단지수를 출력하시오.
- 그리고 각 단지내 집의 수를 오름차순으로 정렬하여 한 줄에 하나씩 출력하시오.
'''

n = int(input())
graph = []
count = []
houses = 0

for _ in range(n):
    graph.append(list(map(int, input())))

def dfs(x, y):
    global houses

    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False
    if graph[x][y] == 0:
        return False
    
    houses += 1 # 집 수 + 1
    graph[x][y] = 0 # 0으로 방문 표시
    dfs(x - 1, y) # 상하좌우 탐색
    dfs(x + 1, y)
    dfs(x, y - 1)
    dfs(x, y + 1)
    return True

for i in range(n):
    for j in range(n):
        if dfs(i, j):
            count.append(houses)
            houses = 0

print(len(count)) # 단지 수 출력
count.sort() # 집의 수 오름차순으로 정렬
print(*count, sep='\n')

# 메모리 31084KB | 시간 72ms | 코드 길이 566B