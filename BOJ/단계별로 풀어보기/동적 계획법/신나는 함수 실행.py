# 신나는 함수 실행
# https://www.acmicpc.net/problem/9184
# 실버 2 | 시간 제한 1초 | 메모리 제한 128MB

'''
재귀 호출만 생각하면 신이 난다! 아닌가요?
다음과 같은 재귀함수 w(a, b, c)가 있다.

if a <= 0 or b <= 0 or c <= 0, then w(a, b, c) returns:
    1

if a > 20 or b > 20 or c > 20, then w(a, b, c) returns:
    w(20, 20, 20)

if a < b and b < c, then w(a, b, c) returns:
    w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)

otherwise it returns:
    w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)

위의 함수를 구현하는 것은 매우 쉽다.
하지만, 그대로 구현하면 값을 구하는데 매우 오랜 시간이 걸린다. (예를 들면, a=15, b=15, c=15)

a, b, c가 주어졌을 때, w(a, b, c)를 출력하는 프로그램을 작성하시오.
'''

'''
입력 조건
- 입력은 세 정수 a, b, c로 이루어져 있으며, 한 줄에 하나씩 주어진다.
- 입력의 마지막은 -1 -1 -1로 나타내며, 세 정수가 모두 -1인 경우는 입력의 마지막을 제외하면 없다.

출력 조건
- 입력으로 주어진 각각의 a, b, c에 대해서, w(a, b, c)를 출력한다.
'''

# 보텀업

import sys
input = sys.stdin.readline

w = [[[0] * 21 for _ in range(21)] for _ in range(21)]

for a in range(21): # w(20, 20, 20)까지 채움
    for b in range(21):
        for c in range(21):
            if a <= 0 or b <= 0 or c <= 0:
                w[a][b][c] = 1
            elif a < b and b < c:
                w[a][b][c] = w[a][b][c - 1] + w[a][b - 1][c - 1] - w[a][b - 1][c]
            else:
                w[a][b][c] = w[a - 1][b][c] + w[a - 1][b - 1][c] + w[a - 1][b][c - 1] - w[a - 1][b - 1][c - 1]

while True:
    a, b, c = map(int, input().split())

    if a == -1 and b == -1 and c == -1:
            break

    if a <= 0 or b <= 0 or c <= 0:
        print("w({}, {}, {}) = 1".format(a, b, c))
    elif a > 20 or b > 20 or c > 20:
        print("w({}, {}, {}) = {}".format(a, b, c, w[20][20][20]))
    else:
        print("w({}, {}, {}) = {}".format(a, b, c, w[a][b][c]))

# 메모리 30840KB | 시간 96ms | 코드 길이 862B

# 탑다운

import sys
input = sys.stdin.readline

d = [[[0] * 21 for _ in range(21)] for _ in range(21)]

def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)

    if d[a][b][c]: # 이미 계산된 결과면 dp 테이블에 저장된 값 리턴
        return d[a][b][c]

    if a < b < c:
        d[a][b][c] = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
    else:
        d[a][b][c] = w(a - 1, b, c) + w(a - 1, b - 1, c) + w(a - 1, b, c - 1) - w(a - 1, b - 1, c - 1)    
        
    return d[a][b][c]

while True:
    a, b, c = map(int, input().split())

    if a == -1 and b == -1 and c == -1:
        break
    print("w({}, {}, {}) = {}".format(a, b, c, w(a, b, c)))

# 메모리 30840KB | 시간 100ms | 코드 길이 681B