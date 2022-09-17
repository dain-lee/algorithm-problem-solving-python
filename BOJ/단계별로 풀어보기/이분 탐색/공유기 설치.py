# 공유기 설치
# https://www.acmicpc.net/problem/2110
# 골드 4 | 시간 제한 2초 | 메모리 제한 128MB

'''
도현이의 집 N개가 수직선 위에 있다.
각각의 집의 좌표는 x1, ..., xN이고, 집 여러개가 같은 좌표를 가지는 일은 없다.
도현이는 언제 어디서나 와이파이를 즐기기 위해서 집에 공유기 C개를 설치하려고 한다.
최대한 많은 곳에서 와이파이를 사용하려고 하기 때문에, 한 집에는 공유기를 하나만 설치할 수 있고, 가장 인접한 두 공유기 사이의 거리를 가능한 크게 하여 설치하려고 한다.
C개의 공유기를 N개의 집에 적당히 설치해서, 가장 인접한 두 공유기 사이의 거리를 최대로 하는 프로그램을 작성하시오.
'''

'''
입력 조건
- 첫째 줄에 집의 개수 N (2 ≤ N ≤ 200,000)과 공유기의 개수 C (2 ≤ C ≤ N)이 하나 이상의 빈 칸을 사이에 두고 주어진다.
- 둘째 줄부터 N개의 줄에는 집의 좌표를 나타내는 xi (0 ≤ xi ≤ 1,000,000,000)가 한 줄에 하나씩 주어진다.

출력 조건
- 첫째 줄에 가장 인접한 두 공유기 사이의 최대 거리를 출력한다.
'''

import sys
input = sys.stdin.readline

n, c = map(int, input().split())
array = [int(input()) for _ in range(n)]
array.sort() # 이분 탐색을 위해 정렬

start = 1
end = array[n - 1] - array[0] # 탐색 범위는 1부터 가장 먼 두 집 사이의 거리 까지
dist = 0

if c == 2: # 설치해야 하는 공유기가 2개면 첫번째 집과 마지막 집에 설치
    print(end)
    exit(0)

while start <= end:
    mid = (start + end) // 2
    prev = array[0]
    total = 1
    for i in array[1:]:
        if i - prev >= mid: # 현재 집과 이전 집 사이의 거리가 mid 보다 크면
            total += 1 # 공유기 설치
            prev = i
    if total >= c: # 공유기가 c개 이상 또는 더 많이 설치됨 => 거리를 늘려야 함
        start = mid + 1
        dist = mid # total == c일 때만 dist를 갱신하면 안됨
    else: # 공유기가 c개 보다 적게 설치됨 => 거리를 줄여야 함
        end = mid - 1

print(dist)

# 메모리 40132KB | 시간 488ms | 코드 길이 501B