n, m, k = map(int, input().split())

array = [list(map(int, input().split())) for _ in range(n)] # 상어 위치
direction = list(map(int, input().split())) # 상어들의 현재 방향
priority = [[] for _ in range(m)] # 상어들 각각의 방향 우선 순위

for i in range(m):
    for _ in range(4):
        data = list(map(int, input().split()))
        priority[i].append(data)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

smell = [[] for _ in range(n)] # 냄새 정보 리스트
for i in range(n):
    for _ in range(n):
        smell[i].append([0, 0]) # [상어 번호, 남은 시간]

def spray(): # 냄새를 뿌리는 함수
    for i in range(n):
        for j in range(n):
            if array[i][j]:
                smell[i][j] = [array[i][j], k]

def find_direction(location): # 다음 이동 방향을 찾는 함수
    next_direction = {}

    for i in location:
        num, x, y = i
        next = 0
        for d in priority[num-1][direction[num-1]-1]: # 우선순위 순서대로 루프를 돌림
            nx = x + dx[d-1]
            ny = y + dy[d-1]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if not (smell[nx][ny][0] == 0 or smell[nx][ny][0] == num): # 냄새가 없거나, 자신의 냄새가 아니면 continue
                continue
            if next != 0 and smell[nx][ny][0] == num: # 방향을 이미 갱신했다면 지금 검사하는 방향이 자신의 냄새가 있는 방향일 경우 우선순위가 무조건 떨어지므로 continue
                continue

            next = d # 다음에 이동할 방향 갱신
            if smell[nx][ny][0] == 0: # 우선순위 순서대로 루프를 돌렸을 때, 아무 냄새가 없는 칸이 가장 우선순위가 높으므로 break
                break
        next_direction[num] = next # {상어 번호 : 다음에 이동할 방향}
    return next_direction

def move_sharks(): # 상어 이동 함수
    time = 0

    while(time <= 1000): # 1000초를 넘기 전까지
        spray() # 자기 자리에 냄새를 뿌림

        location = []
        for i in range(n): # 각 상어들의 위치를 리스트에 저장
            for j in range(n):
                if array[i][j]:
                    location.append((array[i][j], i, j))
        if len(location) == 1: # 리스트의 길이가 1이면 1번 상어만 남은 것이므로, return
            return time
        next_direction = find_direction(location) # 다음에 이동할 방향을 찾음
        for i in location:
            num, x, y = i
            d = next_direction[num]
            nx = x + dx[d-1]
            ny = y + dy[d-1]
            
            array[x][y] = 0
            if array[nx][ny] == 0 or array[nx][ny] > num: # 다음에 이동할 위치가 비어있거나, 자신보다 큰 번호의 상어가 있으면 이동
                array[nx][ny] = num
                direction[num-1] = d

        for i in range(n): # 냄새 정보 리스트를 돌면서 남은 시간에 -1, 남은 시간이 0이면 냄새를 없앰
            for j in range(n):
                smell[i][j][1] -= 1
                if smell[i][j][1] == 0:
                    smell[i][j][0] = 0
        
        time += 1
    return -1

print(move_sharks())

'''
시뮬레이션
상어마다 방향 우선순위 정보가 주어지므로, 모든 방향 정보를 담을 리스트를 별도로 선언
'''

n, m, k = map(int, input().split())

# 모든 상어의 위치와 방향 정보를 포함하는 2차원 리스트
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 모든 상어의 현재 방향 정보
directions = list(map(int, input().split()))

# 각 위치마다 [특정 냄새의 상어 번호, 특정 냄새의 남은 시간]을 저장하는 2차원 리스트
smell = [[[0, 0]] * n for _ in range(n)]

# 각 상어의 회전 방향 우선순위 정보
priorities = [[] for _ in range(m)]
for i in range(m):
    for j in range(4):
        priorities[i].append(list(map(int, input().split())))

# 특정 위치에서 이동 가능한 4가지 방향
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 모든 냄새 정보를 업데이트
def update_smell():
    # 각 위치를 하나씩 확인하며
    for i in range(n):
        for j in range(n):
            # 냄새가 존재하는 경우, 시간을 1만큼 감소시키기
            if smell[i][j][1] > 0:
                smell[i][j][1] -= 1
            # 상어가 존재하는 해당 위치의 냄새를 k로 설정
            if array[i][j] != 0:
                smell[i][j] = [array[i][j], k]

# 모든 상어를 이동시키는 함수
def move():
    # 이동 결과를 담기 위한 임시 결과 테이블 초기화
    new_array = [[0] * n for _ in range(n)]

    # 각 위치를 하나씩 확인하며
    for x in range(n):
        for y in range(n):
            # 상어가 존재하는 경우
            if array[x][y] != 0:
                direction = directions[array[x][y] - 1] # 현재 상어의 방향
                found = False
                # 일단 냄새가 존재하지 않는 곳이 있는지 확인
                for index in range(4):
                    nx = x + dx[priorities[array[x][y] - 1][direction - 1][index] - 1]
                    ny = y + dy[priorities[array[x][y] - 1][direction - 1][index] - 1]
                    if 0 <= nx and nx < n and 0 <= ny and ny < n:
                        if smell[nx][ny][1] == 0: # 냄새가 존재하지 않는 곳이면
                            # 해당 상어의 방향 이동시키기
                            directions[array[x][y] - 1] = priorities[array[x][y] - 1][direction - 1][index]
                            # (만약 이미 다른 상어가 있다면 번호가 낮은 상어가 들어가도록)
                            # 상어 이동시키기
                            if new_array[nx][ny] == 0:
                                new_array[nx][ny] = array[x][y]
                            else:
                                new_array[nx][ny] = min(new_array[nx][ny], array[x][y])
                            found = True
                            break
                if found:
                    continue
                # 주변에 모두 냄새가 남아 있다면, 자신의 냄새가 있는 곳으로 이동
                for index in range(4):
                    nx = x + dx[priorities[array[x][y] - 1][direction - 1][index] - 1]
                    ny = y + dy[priorities[array[x][y] - 1][direction - 1][index] - 1]
                    if 0 <= nx and nx < n and 0 <= ny and ny < n:
                        if smell[nx][ny][0] == array[x][y]: # 자신의 냄새가 있는 곳이면
                            # 해당 상어의 방향 이동시키기
                            directions[array[x][y] - 1] = priorities[array[x][y] - 1][direction - 1][index]
                            # 상어 이동시키기
                            new_array[nx][ny] = array[x][y]
                            break
    return new_array

time = 0
while True:
    update_smell() # 모든 위치의 냄새를 업데이트
    new_array = move() # 모든 상어를 이동시키기
    array = new_array # 맵 업데이트
    time += 1 # 시간 증가

    # 1번 상어만 남았는지 체크
    check = True
    for i in range(n):
        for j in range(n):
            if array[i][j] > 1:
                check = False
    if check:
        print(time)
        break

    # 1,000초가 지날 때까지 끝나지 않았다면
    if time >= 1000:
        print(-1)
        break