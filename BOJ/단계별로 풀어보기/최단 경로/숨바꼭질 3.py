# 숨바꼭질 3
# https://www.acmicpc.net/problem/13549
# 골드 5 | 시간 제한 2초 | 메모리 제한 512MB

'''
수빈이는 동생과 숨바꼭질을 하고 있다.
수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다.
수빈이는 걷거나 순간이동을 할 수 있다.
만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다.
순간이동을 하는 경우에는 0초 후에 2*X의 위치로 이동하게 된다.
수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오.
'''

'''
입력 조건
- 첫 번째 줄에 수빈이가 있는 위치 N과 동생이 있는 위치 K가 주어진다. N과 K는 정수이다.

출력 조건
- 수빈이가 동생을 찾는 가장 빠른 시간을 출력한다.
'''

import heapq

INF = int(1e9)
n, k = map(int, input().split())
time = [INF] * 100001 # 무한으로 초기화

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    time[start] = 0
    while q:
        t, x = heapq.heappop(q)
        if x == k:
            return time[x]

        if time[x] < t: # 기존에 계산했던 값이 더 작으면 넘어감
            continue

        for i in ((1, x-1), (1, x+1), (0, 2*x)): # (가중치, 위치)
            if 0 <= i[1] <= 100000:
                ntime = t + i[0]
                if ntime < time[i[1]]: # 기존 값과 계산한 값 비교
                    time[i[1]] = ntime
                    heapq.heappush(q, (time[i[1]], i[1]))

print(dijkstra(n))

# 메모리 36764KB | 시간 216ms | 코드 길이 582B