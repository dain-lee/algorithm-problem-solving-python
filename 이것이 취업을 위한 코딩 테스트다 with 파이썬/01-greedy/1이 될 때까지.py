# 1이 될 때까지
# 난이도 하 | 시간 제한 1초 | 메모리 제한 128MB | 기출 2018 E 기업 알고리즘 대회

'''
어떠한 수 N이 1이 될 때까지 다음의 두 과정 중 하나를 반복적으로 선택하여 수행하려고 한다.
단, 두 번째 연산은 N이 K로 나누어덜어질 때만 선택할 수 있다.
1. N에서 1을 뺀다.
2. N을 K로 나눈다.

예를 들어 N이 17, K가 4라고 가정하자. 이때 1번의 과정을 한 번 수행하면 N은 16이 된다.
이후에 2번의 과정을 두 번 수행하면 N은 1이 된다.
결과적으로 이 경우 전체 과정을 실행한 횟수는 3이 된다.
이는 N을 1로 만드는 최소 횟수이다.
N과 K가 주어질 때 N이 1이 될 때까지 1번 혹은 2번의 과정을 수행해야 하는 최소 횟수를 구하는 프로그램을 작성하시오.
'''

'''
입력 조건
- 첫째 줄에 N(2 <= N <= 100,000)과 K(2 <= k <= 100,000)가 공백으로 구분되며 각각 자연수로 주어진다.
  이때 입력으로 주어지는 N은 항상 K보다 크거나 같다.

출력 조건
- 첫째 줄에 N이 1이 될 때까지 1번 혹은 2번의 과정을 수행해야 하는 횟수의 최솟값을 출력한다.
'''

n, k = map(int, input().split())

count = 0
while n != 1:
    if n%k == 0:
        n //= k
        count += 1
    else:
        n -= 1
        count += 1

print(count)


# 문제 해설

'''
'최대한 많이 나누기' 수행
'''

n, k = map(int, input().split())
result = 0

# N이 K 이상이라면 K로 계속 나누기
while n >= k:
    # N이 K로 나누어 떨어지지 않는다면 N에서 1씩 빼기
    while n % k != 0:
        n -= 1
        result += 1
    # K로 나누기
    n //= k
    result += 1

# 마지막으로 남은 수에 대하여 1씩 빼기
while n > 1:
    n -= 1
    result += 1

print(result)


# N이 K의 배수가 되도록 효율적으로 한 번에 빼는 방식
n, k = map(int, input().split())
result = 0

while True:
    # (N == K로 나누어 떨어지는 수)가 될 때까지 1씩 빼기
    target = (n // k) * k
    result += (n - target)
    n = target
    # N이 K보다 작을 때(더 이상 나눌 수 없을 때) 반복문 탈출
    if n < k:
        break
    # K로 나누기
    result += 1
    n //= k

# 마지막으로 남은 수에 대하여 1씩 빼기
result += (n - 1)
print(result)