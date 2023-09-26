from collections import deque

def solution(maps):
    
    list_maps = []
    for map in maps:
        list_maps.append(list(map))
    
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    answer = []
    
    def bfs(x, y):
        food = int(list_maps[x][y])
        list_maps[x][y] = 'X'
        queue = deque([(x, y)])
        
        while queue:
            x, y = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if nx < 0 or nx >= len(list_maps) or ny < 0 or ny >= len(list_maps[0]):
                    continue
                if list_maps[nx][ny] == 'X':
                    continue
                
                food += int(list_maps[nx][ny])
                list_maps[nx][ny] = 'X'
                queue.append((nx, ny))
        return food
    
    for i in range(len(list_maps)):
        for j in range(len(list_maps[0])):
            if list_maps[i][j] != 'X':
                answer.append(bfs(i, j))
    
    if len(answer) == 0:
        answer.append(-1)
        
    return sorted(answer)