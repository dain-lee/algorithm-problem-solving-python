# 금광
# 난이도 중하 | 풀이 시간 30분 | 시간 제한 1초 | 메모리 제한 128MB

'''
n x m 크기의 금광이 있습니다.
금광은 1 x 1 크기의 칸으로 나누어져 있으며, 각 칸은 특정한 크기의 금이 들어 있습니다.
채굴자는 첫 번째 열부터 출발하여 금을 캐기 시작합니다.
맨 처음에는 첫번째 열의 어느 행에서든 출발할 수 있습니다.
이후에 m번에 걸쳐서 매번 오른쪽 위, 오른쪽, 오른쪽 아래 3가지 중 하나의 위치로 이동해야 합니다.
결과적으로 채굴자가 얻을 수 있는 금의 최대 크기를 출력하는 프로그램을 작성하세요.

만약 다음과 같이 3 x 4 크기의 금광이 존재한다고 가정합시다.
1 3 3 2
2 1 4 1
0 6 4 7
가장 왼쪽 위치를 (1, 1), 가장 오른쪽 위치를 (n, m)이라고 할 때,
위 예시에서는 (2, 1) -> (3, 2) -> (3, 3) -> (3, 4)의 위치로 이동하면 총 19만큼의 금을 채굴할 수 있으며, 이때의 값이 최댓값입니다.
'''

'''
입력 조건
- 첫째 줄에 테스트 케이스 T가 입력됩니다. (1 <= T <= 1000)
- 매 테스트 케이스 첫째 줄에 n과 m이 공백으로 구분되어 입력됩니다. (1 <= n, m <= 20)
- 둘째 줄에 n x m개의 위치에 매장된 금의 개수가 공백으로 구분되어 입력됩니다. (0 <= 각 위치에 매장된 금의 개수 <= 100)

출력 조건
- 테스트 케이스마다 채굴자가 얻을 수 있는 금의 최대 크기를 출력합니다.
- 각 테스트 케이스는 줄 바꿈을 이용해 구분합니다.
'''

# 큐 사용
from collections import deque

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    data = list(map(int, input().split()))
    array = []

    for i in range(0, len(data)-m+1, m):
        array.append(data[i:i+m])
    
    gold = [[0] * m for _ in range(n)]
    dx = [-1, 0, 1]

    for i in range(n):
        queue = deque([(i, 0)])
        gold[i][0] = array[i][0]
        
        while queue:
            x, y = queue.popleft()
            for j in range(3):
                nx = x + dx[j]
                ny = y + 1
                if 0 <= nx < n and 0 <= ny < m:
                    if gold[x][y] + array[nx][ny] > gold[nx][ny]:
                        gold[nx][ny] = gold[x][y] + array[nx][ny]
                        queue.append((nx, ny))
    
    result = 0
    for i in range(n):
        if gold[i][m - 1] > result:
            result = gold[i][m - 1]
    print(result)


'''
금광의 모든 위치에 대하여,
1. 왼쪽 위에서 오는 경우
2. 왼쪽 아래에서 오는 경우
3. 왼쪽에서 오는 경우
위 3 가지 경우만 존재한다.
dp[i][j] = array[i][j] + max(dp[i-1][j-1], dp[i][j - 1], dp[i+1][j-1])
'''

for tc in range(int(input())):
    n, m = map(int, input().split())
    array = list(map(int, input().split()))

    # 다이나믹 프로그래밍을 위한 2차원 DP 테이블 초기화
    dp = []
    index = 0
    for i in range(n):
        dp.append(array[index:index+m])
        index += m
    
    # 다이나믹 프로그래밍 진행
    for j in range(1, m):
        for i in range(n):
            # 왼쪽 위에서 오는 경우
            if i == 0: # 첫번째 행일 경우
                left_up = 0
            else:
                left_up = dp[i - 1][j - 1]
            # 왼쪽 아래에서 오는 경우
            if i == n - 1: # 마지막 행일 경우
                left_down = 0
            else:
                left_down = dp[i + 1][j - 1]
            # 왼쪽에서 오는 경우
            left = dp[i][j - 1]
            dp[i][j] = dp[i][j] + max(left_up, left_down, left)
    
    result = 0
    for i in range(n):
        result = max(result, dp[i][m - 1])
    
    print(result)