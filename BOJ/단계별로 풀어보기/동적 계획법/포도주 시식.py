# 포도주 시식
# https://www.acmicpc.net/problem/2156
# 실버 1 | 시간 제한 2초 | 메모리 제한 128MB

'''
효주는 포도주 시식회에 갔다.
그 곳에 갔더니, 테이블 위에 다양한 포도주가 들어있는 포도주 잔이 일렬로 놓여 있었다.
효주는 포도주 시식을 하려고 하는데, 여기에는 다음과 같은 두 가지 규칙이 있다.
포도주 잔을 선택하면 그 잔에 들어있는 포도주는 모두 마셔야 하고, 마신 후에는 원래 위치에 다시 놓아야 한다.
연속으로 놓여 있는 3잔을 모두 마실 수는 없다.
효주는 될 수 있는 대로 많은 양의 포도주를 맛보기 위해서 어떤 포도주 잔을 선택해야 할지 고민하고 있다.
1부터 n까지의 번호가 붙어 있는 n개의 포도주 잔이 순서대로 테이블 위에 놓여 있고, 각 포도주 잔에 들어있는 포도주의 양이 주어졌을 때, 효주를 도와 가장 많은 양의 포도주를 마실 수 있도록 하는 프로그램을 작성하시오. 
예를 들어 6개의 포도주 잔이 있고, 각각의 잔에 순서대로 6, 10, 13, 9, 8, 1 만큼의 포도주가 들어 있을 때, 첫 번째, 두 번째, 네 번째, 다섯 번째 포도주 잔을 선택하면 총 포도주 양이 33으로 최대로 마실 수 있다.
'''

'''
입력 조건
- 첫째 줄에 포도주 잔의 개수 n이 주어진다. (1 ≤ n ≤ 10,000)
- 둘째 줄부터 n+1번째 줄까지 포도주 잔에 들어있는 포도주의 양이 순서대로 주어진다.
- 포도주의 양은 1,000 이하의 음이 아닌 정수이다.

출력 조건
- 첫째 줄에 최대로 마실 수 있는 포도주의 양을 출력한다.
'''

import sys
input = sys.stdin.readline

n = int(input())
array = []

for _ in range(n):
    array.append(int(input()))

if n == 1:
    print(array[0])
    exit(0)

# 계단 오르기 문제와 다른 점은 마지막 잔을 마시지 않아도 된다는 것, 2번 이상 연속해서 건너뛰어도 된다는 것
d = [[0] * 3 for _ in range(n)]
d[0][1] = array[0]
d[1][0] = array[0] # 건너뛰는 경우
d[1][1] = array[1] # 첫번째 연속된 잔을 마시는 경우
d[1][2] = array[0] + array[1] # 두번째 연속된 잔을 마시는 경우

for i in range(2, n):
    d[i][0] = max(d[i - 1])
    d[i][1] = max(d[i - 2]) + array[i]
    d[i][2] = d[i - 1][1] + array[i]

print(max(d[n - 1]))
# 메모리 31860KB | 시간 84ms | 코드 길이 430B

# 점화식을 세우는 방법
import sys
input = sys.stdin.readline

n = int(input())
array = [int(input()) for _ in range(n)]

if n == 1:
    print(array[0])
else:
    d = [0] * n
    d[0] = array[0]
    d[1] = array[0] + array[1]
    d[2] = max(array[0] + array[2], array[1] + array[2], d[1])

    for i in range(3, n):
        # i - 1번째 포도주를 마시지 않고 i번째 포도주를 마신 경우 / i - 1번째, i번째 포도주를 마신 경우 / i번째 포도주를 마시지 않은 경우
        d[i] = max(array[i] + d[i - 2], array[i] + array[i - 1] + d[i - 3], d[i - 1])

    print(d[n - 1])