# 수 정렬하기 3
# https://www.acmicpc.net/problem/10989
# 브론즈 1 | 시간 제한 5초 | 메모리 제한 8MB

'''
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.
'''

'''
입력 조건
- 첫째 줄에 수의 개수 N(1 ≤ N ≤ 10,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수가 주어진다. 이 수는 10,000보다 작거나 같은 자연수이다.

출력 조건
- 첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.
'''

import sys
input = sys.stdin.readline

n = int(input())
array = [0] * 10001 # 10,000보다 작거나 같은 자연수이므로

for _ in range(n):
    array[int(input())] += 1 # 계수 정렬

for i in range(10001):
    for j in range(array[i]):
        print(i)

# 메모리 30840KB | 시간 8868ms | 코드 길이 195B