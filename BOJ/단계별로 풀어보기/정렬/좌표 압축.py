# 좌표 압축
# https://www.acmicpc.net/problem/18870
# 실버 2 | 시간 제한 2초 | 메모리 제한 512MB

'''
수직선 위에 N개의 좌표 X1, X2, ..., XN이 있다. 이 좌표에 좌표 압축을 적용하려고 한다.
Xi를 좌표 압축한 결과 X'i의 값은 Xi > Xj를 만족하는 서로 다른 좌표의 개수와 같아야 한다.
X1, X2, ..., XN에 좌표 압축을 적용한 결과 X'1, X'2, ..., X'N를 출력해보자.
'''

'''
입력 조건
- 첫째 줄에 N이 주어진다.
- 둘째 줄에는 공백 한 칸으로 구분된 X1, X2, ..., XN이 주어진다.

출력 조건
- 첫째 줄에 X'1, X'2, ..., X'N을 공백 한 칸으로 구분해서 출력한다.
'''

import sys
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))
sorted_array = sorted(set(array))

# for i in array:
#     print(sorted_array.index(i), end=' ')
# 시간 초과 - list.index(i)는 시간복잡도 O(N)

dict = {sorted_array[i] : i for i in range(len(sorted_array))} # key 값으로 좌표값, value 값으로 인덱스
for i in array:
    print(dict[i], end = ' ') # dict[i]는 시간복잡도 O(1)

# 메모리 156812KB | 시간 2204ms | 코드 길이 238B