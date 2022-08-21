# 분해합
# https://www.acmicpc.net/problem/2231
# 브론즈 2 | 시간 제한 2초 | 메모리 제한 192MB

'''
어떤 자연수 N이 있을 때, 그 자연수 N의 분해합은 N과 N을 이루는 각 자리수의 합을 의미한다.
어떤 자연수 M의 분해합이 N인 경우, M을 N의 생성자라 한다.
예를 들어, 245의 분해합은 256(=245+2+4+5)이 된다.
따라서 245는 256의 생성자가 된다.
물론, 어떤 자연수의 경우에는 생성자가 없을 수도 있다.
반대로, 생성자가 여러 개인 자연수도 있을 수 있다.
자연수 N이 주어졌을 때, N의 가장 작은 생성자를 구해내는 프로그램을 작성하시오.
'''

'''
입력 조건
- 첫째 줄에 자연수 N(1 ≤ N ≤ 1,000,000)이 주어진다.

출력 조건
- 첫째 줄에 답을 출력한다. 생성자가 없는 경우에는 0을 출력한다.
'''

n = int(input())
result = 0

for i in range(1, n):
    temp_i = i # 현재 i값 저장
    temp_sum = i
    while i > 0: # 분해합
        temp_sum += i % 10
        i //= 10
    if temp_sum == n:
        result = temp_i
        break

print(result)

# list 활용
n = int(input())
result = 0

for i in range(1, n):
    temp = i + sum(map(int, str(i))) # i를 리스트로 변환
    if temp == n:
        result = i
        break

print(result)

# 메모리 30840KB | 시간 1252ms | 코드 길이 153B