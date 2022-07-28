'''
파이썬 표준 라이브러리 https://docs.python.org/ko/3/library/index.html

- 내장함수 : print(), input()과 같은 기본 입출력 기능부터 sorted()와 같은 정렬 기능을 포함하고 있는 기본 내장 라이브러리
- itertools : 파이썬에서 반복되는 형태의 데이터를 처리하는 기능을 제공하는 라이브러리. 순열과 조합 라이브러리 제공
- heapq : 힙 기능을 제공하는 라이브러리. 우선순위 큐 기능을 구현하기 위해 사용
- bisect : 이진 탐색 기능을 제공하는 라이브러리
- collections : 덱(deque), 카운터(Counter) 등의 자료구조를 포함하고 있는 라이브러리
- math : 팩토리얼, 제곱근, 최대공약수(GCD), 삼각함수 관련 함수부터 파이(pi)와 같은 상수 등 필수적인 수학적 기능을 제공하는 라이브러리
'''

### 내장 함수 ###

# sum() - iterable 객체가 입력으로 주어졌을 때, 모든 원소의 합을 반환
result = sum([1, 2, 3, 4, 5])
print(result) # 15

# min() - 파라미터가 2개 이상 들어왔을 때 가장 작은 값을 반환
result = min(7, 3, 5, 2)
print(result) # 2

# max() - 파라미터가 2개 이상 들어왔을 때 가장 큰 값을 반환
result = max(7, 3, 5, 2)
print(result) # 7

# eval() - 수학 수식이 문자열 형식으로 들어오면 해당 수식을 계산한 결과를 반환
result = eval("(3 + 5) * 7")
print(result) # 56

# sorted() - iterable 객체가 들어왔을 때, 정렬된 결과를 반환
result = sorted([9, 1, 8, 5, 4])
print(result) # [1, 4, 5, 8, 9]
result = sorted([9, 1, 8, 5, 4], reverse = True)
print(result) # [9, 8, 5, 4, 1]

# 튜플의 두 번째 원소를 기준으로 내림차순으로 정렬
result = sorted([('홍길동', 35), ('이순신', 75), ('아무개', 50)], key = lambda x: x[1], reverse = True)
print(result) # [('이순신', 75), ('아무개', 50), ('홍길동', 35)]


### itertools ###

# permutations - iterable 객체에서 r개의 데이터를 뽑아 일렬로 나열하는 모든 경우(순열) 계산
from itertools import permutations

data = ['A', 'B', 'C']
result = list(permutations(data, 3))
print(result) # [('A', 'B', 'C'), ('A', 'C', 'B'), ('B', 'A', 'C'), ('B', 'C', 'A'), ('C', 'A', 'B'), ('C', 'B', 'A')]

# combinations - iterable 객체에서 r개의 데이터를 뽑아 순서를 고려하지 않고 나열하는 모든 경우(조합) 계산
from itertools import combinations

data = ['A', 'B', 'C']
result = list(combinations(data, 2))
print(result) # [('A', 'B'), ('A', 'C'), ('B', 'C')]

# product - iterable 객체에서 r개의 데이터를 뽑아 일렬로 나열하는 모든 경우(순열) 계산, 중복 허용
from itertools import product

data = ['A', 'B', 'C']
result = list(product(data, repeat = 2))
print(result) # [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'B'), ('B', 'C'), ('C', 'A'), ('C', 'B'), ('C', 'C')]

# combinations_with_replacement - iterable 객체에서 r개의 데이터를 뽑아 순서를 고려하지 않고 나열하는 모든 경우(조합) 계산, 중복 허용
from itertools import combinations_with_replacement

data = ['A', 'B', 'C']
result = list(combinations_with_replacement(data, 2))
print(result) # ('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'B'), ('B', 'C'), ('C', 'C')]


### heapq ###

'''
파이썬의 힙은 최소 힙으로 구성되어 있으므로 단순히 원소를 힙에 전부 넣었다가 빼는 것만으로도
시간 복잡도 O(NlogN)에 오름차순 정렬이 완료됨
힙에 원소를 삽입할 때는 heapq.heappush(), 힙에서 원소를 꺼내고자 할 때는 heapq.heappop()
'''

# 힙 정렬
import heapq

def heapsort(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, value)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for _ in range(len(h)):
        result.append(heapq.heappop(h))
    return result

result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 내림차순 힙 정렬
import heapq

def heapsort(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, -value)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for _ in range(len(h)):
        result.append(-heapq.heappop(h))
    return result

result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result) # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]


### bisect ###

'''
bisect_left() 함수와 bisect_right() 함수는 시간 복잡도 O(logN)에 동작
bisect_left(a, x) : 정렬된 순서를 유지하면서 리스트 a에 데이터 x를 삽입할 가장 왼쪽 인덱스를 찾는 메서드
bisect_right(a, x) : 정렬된 순서를 유지하도록 리스트 a에 데이터 x를 삽입할 가장 오른쪽 인덱스를 찾는 메서드
'''

from bisect import bisect_left, bisect_right

a = [1, 2, 4, 4, 8]
x = 4

print(bisect_left(a, x)) # 2
print(bisect_right(a, x)) # 4

# 정렬된 리스트에서 값이 특정 범위에 속하는 원소의 개수를 구하고자 하는 경우
from bisect import bisect_left, bisect_right

# 값이 [left_value, right_value]인 데이터의 개수를 반환하는 함수
def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index

a = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]
# 값이 4인 데이터 개수 출력
print(count_by_range(a, 4, 4)) # 2
# 값이 [-1, 3] 범위에 있는 데이터 개수 출력
print(count_by_range(a, -1, 3)) # 6


### collections ###

'''
리스트에서 가장 뒤쪽에 원소를 추가하거나, 제거하는 경우 시간 복잡도는 O(1) 이지만,
가장 앞쪽에 원소를 추가하거나, 제거하는 경우 시간 복잡도는 O(N)
deque에서는 가장 앞쪽이나 뒤쪽에 원소를 추가하거나 제거하는 경우 모두 시간 복잡도 O(1)
deque에서는 리스트 자료형과 다르게 인덱싱, 슬라이싱 등의 기능은 사용할 수 없음
첫 번째 원소를 제거할 때 popleft() 사용, 마지막 원소를 제거할 때 pop() 사용
첫 번째 인덱스에 원소 x를 삽입할 때 appendleft(x) 사용, 마지막 인덱스에 원소를 삽입할 때 append(x) 사용
'''

from collections import deque

data = deque([2, 3, 4])
data.appendleft(1)
data.append(5)

print(data) # deque([1, 2, 3, 4, 5])
print(list(data)) # [1, 2, 3, 4, 5]

'''
collections 라이브러리의 Counter는 등장 횟수를 세는 기능 제공
iterable 객체가 주어졌을 때, 해당 객체 내부의 원소가 몇 번씩 등장했는지를 알려줌
'''

from collections import Counter

counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])

print(counter['blue']) # 3
print(counter['green']) # 1
print(dict(counter)) # {'red': 2, 'blue': 3, 'green': 1}


### math ###

# factorial(x) - x! 값 반환
import math

print(math.factorial(5)) # 120

# sqrt(x) - x의 제곱근 반환
import math

print(math.sqrt(7)) # 2.6457513110645907

# gcd(a, b) - a와 b의 최대 공약수 반환
import math

print(math.gcd(21, 14)) # 7

# pi, e
import math

print(math.pi)
print(math.e)