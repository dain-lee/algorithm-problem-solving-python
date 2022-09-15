# 숫자 카드 2
# https://www.acmicpc.net/problem/10816
# 실버 4 | 시간 제한 1초 | 메모리 제한 256MB

'''
숫자 카드는 정수 하나가 적혀져 있는 카드이다.
상근이는 숫자 카드 N개를 가지고 있다.
정수 M개가 주어졌을 때, 이 수가 적혀있는 숫자 카드를 상근이가 몇 개 가지고 있는지 구하는 프로그램을 작성하시오.
'''

'''
입력 조건
- 첫째 줄에 상근이가 가지고 있는 숫자 카드의 개수 N(1 ≤ N ≤ 500,000)이 주어진다.
- 둘째 줄에는 숫자 카드에 적혀있는 정수가 주어진다. 숫자 카드에 적혀있는 수는 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다.
- 셋째 줄에는 M(1 ≤ M ≤ 500,000)이 주어진다.
- 넷째 줄에는 상근이가 몇 개 가지고 있는 숫자 카드인지 구해야 할 M개의 정수가 주어지며, 이 수는 공백으로 구분되어져 있다. 이 수도 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다.

출력 조건
- 첫째 줄에 입력으로 주어진 M개의 수에 대해서, 각 수가 적힌 숫자 카드를 상근이가 몇 개 가지고 있는지를 공백으로 구분해 출력한다.
'''

from collections import Counter

n = int(input())
array = list(map(int, input().split()))

m = int(input())
x = list(map(int, input().split()))

cnt = Counter(array) # Counter 이용

for i in x:
    print(cnt[i], end=' ')

# 메모리 114480KB | 시간 1012ms | 코드 길이 205B

import bisect

n = int(input())
array = list(map(int, input().split()))
array.sort()

m = int(input())
x = list(map(int, input().split()))

for i in x:
    left = bisect.bisect_left(array, i) # bisect 이용
    right = bisect.bisect_right(array, i)
    print(right-left, end=' ')

# 메모리 114300KB | 시간 1604ms | 코드 길이 264B