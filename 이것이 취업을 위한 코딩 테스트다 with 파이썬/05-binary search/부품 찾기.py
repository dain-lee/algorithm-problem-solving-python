# 부품 찾기
# 난이도 중하 | 풀이 시간 30분 | 시간 제한 1초 | 메모리 제한 128MB

'''
동빈이네 전자 매장에는 부품이 N개 있다.
각 부품은 정수 형태의 고유한 번호가 있다.
어느 날 손님이 M개 종류의 부품을 대량으로 구매하겠다며 당일 날 견적서를 요청했다.
동빈이는 때를 놓치지 않고 손님이 문의한 부품 M개 종류를 모두 확인해서 견적서를 작성해야 한다.
이때 가게 안에 부품이 모두 있는지 확인하는 프로그램을 작성해보자.

예를 들어 가게의 부품이 총 5개일 때 부품 번호가 다음과 같다고 하자.
N = 5
[8, 3, 7, 9, 2]

손님은 총 3개의 부품이 있는지 확인 요청했는데 부품 번호는 다음과 같다.
M = 3
[5, 7, 9]

이때 손님이 요청한 부품 번호의 순서대로 부품을 확인해 부품이 있으면 yes를, 없으면 no를 출력한다.
구분은 공백으로 한다.
'''

'''
입력 조건
- 첫째 줄에 정수 N이 주어진다. (1 <= N <= 1,000,000)
- 둘째 줄에는 공백으로 구분하여 N개의 정수가 주어진다. 이때 정수는 1보다 크고 1,000,000 이하이다.
- 셋째 줄에는 정수 M이 주어진다. (1 <= M <= 100,000)
- 넷째 줄에는 공백으로 구분하여 M개의 정수가 주어진다. 이때 정수는 1보다 크고 1,000,000 이하이다.

출력 조건
- 첫째 줄에 공백으로 구분하여 각 부품이 존재하면 yes를, 없으면 no를 출력한다.
'''

'''
부품을 찾는 과정에서 최악의 경우 시간 복잡도 O(M X logN)의 연산이 필요하므로 이론상 최대 약 200만 번의 연산이 이루어짐
오히려 N개의 부품을 정렬하기 위해서 요구되는 시간 복잡도 O(N X logN)이 이론적으로 최대 약 2,000만으로 더욱더 많은 연산이 필요
결과적으로 이진 탐색을 사용하는 문제 풀이 방법의 경우 시간 복잡도는 O((M + N) X logN)
'''

# 이진 탐색
import sys
input = sys.stdin.readline

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

n = int(input())
array = list(map(int, input().split()))
array.sort() # 이진 탐색을 수행하기 위해 사전에 정렬 수행

m = int(input())
x = list(map(int, input().split()))

# 손님이 확인 요청한 부품 번호를 하나씩 확인
for i in x:
    result = binary_search(array, i, 0, n - 1)
    if result == None:
        print("no", end=' ')
    else:
        print("yes", end=' ')


# 계수 정렬
n = int(input())
array = [0] * 1000001

# 가게에 있는 전체 부품 번호를 입력받아서 기록
for i in input().split():
    array[int(i)] = 1

m = int(input())
x = list(map(int, input().split()))

for i in x:
    if array[i] == 1:
        print("yes", end=' ')
    else:
        print("no", end=' ')


# 집합 자료형
n = int(input())
array = set(map(int, input().split()))

m = int(input())
x = list(map(int, input().split()))

for i in x:
    if i in array: # 리스트의 x in list는 O(n)이지만 집합의 x in set은 O(1)
        print("yes", end=' ')
    else:
        print("no", end=' ')