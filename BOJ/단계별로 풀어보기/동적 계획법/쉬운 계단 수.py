# 쉬운 계단 수
# https://www.acmicpc.net/problem/10844
# 실버 1 | 시간 제한 1초 | 메모리 제한 256MB

'''
45656이란 수를 보자.
이 수는 인접한 모든 자리의 차이가 1이다.
이런 수를 계단 수라고 한다.
N이 주어질 때, 길이가 N인 계단 수가 총 몇 개 있는지 구해보자.
0으로 시작하는 수는 계단수가 아니다.
'''

'''
입력 조건
- 첫째 줄에 N이 주어진다. N은 1보다 크거나 같고, 100보다 작거나 같은 자연수이다.

출력 조건
- 첫째 줄에 정답을 1,000,000,000으로 나눈 나머지를 출력한다.
'''

# https://cotak.tistory.com/12 참고

n = int(input())
d = [[0] * 10 for _ in range(n + 1)] # d[자리 수][현재 수]

for i in range(1, 10):
    d[1][i] = 1 # 1자리일 때 경우의 수

for i in range(2, n + 1):
    for j in range(10):
        if j == 0: # 현재 자리 수가 0이면 직전 자리 수가 무조건 1이어야 함
            d[i][j] = d[i - 1][1]
        elif j == 9: # 현재 자리 수가 9면 직전 자리 수가 무조건 8이어야 함
            d[i][j] = d[i - 1][8]
        else: # 1~8은 직전 자리 수가 j - 1, j + 1이 올 수 있음
            d[i][j] = d[i - 1][j - 1] + d[i - 1][j + 1]

print(sum(d[n]) % 1000000000)

# 메모리 30840KB | 시간 72ms | 코드 길이 353B