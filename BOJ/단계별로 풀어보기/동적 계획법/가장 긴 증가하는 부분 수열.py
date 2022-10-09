# 가장 긴 증가하는 부분 수열
# https://www.acmicpc.net/problem/11053
# 실버 2 | 시간 제한 1초 | 메모리 제한 256MB

'''
수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.
예를 들어, 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에 가장 긴 증가하는 부분 수열은 A = {10, 20, 10, 30, 20, 50} 이고, 길이는 4이다.
'''

'''
입력 조건
- 첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000)이 주어진다.
- 둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. (1 ≤ Ai ≤ 1,000)

출력 조건
- 첫째 줄에 수열 A의 가장 긴 증가하는 부분 수열의 길이를 출력한다.
'''

# LIS dp 테이블 이용
import sys
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))
d = [1] * n # dp테이블은 해당 수가 증가하는 수열의 마지막 수인 경우 / 1로 초기화

for i in range(n):
    for j in range(i): # 이전 수와 하나하나 비교
        if array[i] > array[j]: # 현재 수보다 이전의 수가 더 작으면
            d[i] = max(d[i], d[j] + 1) # 이전 수의 dp 테이블 값 + 1과 현재 수의 dp 테이블 값 중 큰 수 저장

print(max(d))