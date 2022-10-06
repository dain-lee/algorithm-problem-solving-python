# 알고리즘 수업 - 피보나치 수 1
# https://www.acmicpc.net/problem/24416
# 브론즈 1 | 시간 제한 1초 | 메모리 제한 512MB

'''
오늘도 서준이는 동적 프로그래밍 수업 조교를 하고 있다.
아빠가 수업한 내용을 학생들이 잘 이해했는지 문제를 통해서 확인해보자.
오늘은 n의 피보나치 수를 재귀호출과 동적 프로그래밍으로 구하는 알고리즘을 배웠다.
재귀호출에 비해 동적 프로그래밍이 얼마나 빠른지 확인해 보자.
아래 의사 코드를 이용하여 n의 피보나치 수를 구할 경우 코드1 코드2 실행 횟수를 출력하자.

피보나치 수 재귀호출 의사 코드는 다음과 같다.

fib(n) {
    if (n = 1 or n = 2)
    then return 1;  # 코드1
    else return (fib(n - 1) + fib(n - 2));
}
피보나치 수 동적 프로그래밍 의사 코드는 다음과 같다.

fibonacci(n) {
    f[1] <- f[2] <- 1;
    for i <- 3 to n
        f[i] <- f[i - 1] + f[i - 2];  # 코드2
    return f[n];
}
'''

'''
입력 조건
- 첫째 줄에 n(5 ≤ n ≤ 40)이 주어진다.

출력 조건
- 코드1 코드2 실행 횟수를 한 줄에 출력한다.
'''

def fib(n): # 재귀 함수
    global r
    if n == 1 or n == 2:
        r += 1
        return 1 # 코드 1
    return fib(n - 1) + fib(n - 2)

def fibonacci(n): # DP
    global d
    for i in range(3, n + 1):
        d += 1
        f[i] = f[i - 1] + f[i - 2] # 코드 2
    return f[n]

n = int(input())
f = [0] * (n + 1)
f[1] = 1
f[2] = 1
r = 0
d = 0

fib(n)
fibonacci(n)

print(r, d)

# 다른 풀이
def fibonacci(n):
    for i in range(3, n + 1):
        f[i] = f[i - 1] + f[i - 2]
    return f[n]

n = int(input())
f = [0] * (n + 1)
f[1] = 1
f[2] = 1

# 재귀 코드 1 실행 횟수는 f[n](n의 피보나치 수)과 같음
# DP 코드 2 실행 횟수는 1, 2를 제외한 3부터 n까지 for문 반복 횟수 이므로 n - 2
print(fibonacci(n), n - 2)

# 메모리 30840KB | 시간 68ms | 코드 길이 180B