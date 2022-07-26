### 수 자료형 ###

'''
유효숫자e지수 = 유효숫자 * 10**지수
'''

# 1000000000.0
a = 1e9
print(a)

# 752.5
a = 75.25e1
print (a)

# 3.954
a = 3954e-3
print(a)

'''
소수점 값을 비교하는 작업이 필요한 문제라면 round() 함수 이용
round(실수형 데이터, 반올림하고자 하는 위치 - 1)
123.456을 소수점 셋째 자리에서 반올림하려면 round(123.456, 2)
'''

# 0.8999999999999999
a = 0.3 + 0.6
print(a)

# 0.9
a = 0.3 + 0.6
print(round(a, 4))


### 리스트 자료형 ###

# 빈 리스트 선언 방법 1
a = list()

# 빈 리스트 선언 방법 2
a = []

# 크기가 N이고, 모든 값이 0인 1차원 리스트 초기화 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
n = 10
a = [0] * n
print(a)

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# 뒤에서 첫 번째 원소 출력
print(a[-1])

# 두 번째 원소부터 네 번째 원소까지
print(a[1 : 4])

'''
리스트 컴프리헨션을 이용하면 대괄호 안에 조건문과 반복문을 넣는 방식으로 리스트를 초기화할 수 있음
'''

# 0부터 19까지의 수 중에서 홀수만 포함하는 리스트
array = [i for i in range(20) if i % 2 == 1]
print(array)

# 1부터 9까지의 수의 제곱 값을 포함하는 리스트
array = [i * i for i in range(1, 10)]
print(array)

# N X M 크기의 2차원 리스트 초기화
n = 3
m = 4
array = [[0] * m for _ in range(n)]
print(array)

'''
반복을 수행하되 반복을 위한 변수의 값을 무시하고자 할 때 언더바 (_) 사용
for _ in range(5):
    print("Hello World")
'''

a = [1, 4, 3]

# 리스트에 원소 삽입 - 시간 복잡도 O(1)
a.append(2)
print("삽입: ", a)

# 오름차순 정렬 - 시간 복잡도 O(NlogN)
a.sort()
print("오름차순 정렬: ", a)

# 내림차순 정렬 - 시간 복잡도 O(NlogN)
a.sort(reverse = True)
print("내림차순 정렬: ", a)

# 리스트 원소 뒤집기 - 시간 복잡도 O(N)
a.reverse()
print("원소 뒤집기: ", a)

# 특정 인덱스에 데이터 추가 - 시간 복잡도 O(N)
a.insert(2, 3)
print("인덱스 2에 3 추가: ", a)

# 특정 값인 데이터 개수 세기 - 시간 복잡도 O(N)
print("값이 3인 데이터 개수: ", a.count(3))

# 특정 값 데이터 삭제 - 시간 복잡도 O(N)
a.remove(1)
print("값이 1인 데이터 삭제: ", a)

'''
파이썬의 경우 remove_all()과 같은 함수를 기본적으로 제공해주지 않으므로 특정한 값의 원소를 모두 제거하려면 set 활용
'''

a = [1, 2, 3, 4, 5, 5, 5]
remove_set = {3, 5}

#remove_set에 포함되지 않은 값만을 저장 [1, 2, 4]
result = [i for i in a if i not in remove_set]
print(result)


### 문자열 자료형 ###

# Hello World
a = "Hello"
b = "World"
print(a + " " + b)

# StringStringString
a = "String"
print(a * 3)

# CD
a = "ABCDEF"
print(a[2 : 4])


### 튜플 자료형 ###

'''
튜플은 한 번 선언된 값을 변경할 수 없음
리스트는 대괄호([])를 이용하지만, 튜플은 소괄호(())를 이용
'''
a = (1, 2, 3, 4)
print(a)


### 사전 자료형 ###

'''
키와 값의 쌍을 데이터로 가짐
파이썬의 사전 자료형은 내부적으로 해시 테이블을 이용하므로 기본적으로 데이터의 검색 및 수정에 있어서 O(1)의 시간에 처리할 수 있음
키-값 쌍으로 구성된 데이터를 처리함에 있어서 리스트보다 훨씬 빠르게 동작
'''

data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'
data['코코넛'] = 'Coconut'

# 키 데이터만 담은 리스트
key_list = data.keys()
# 값 데이터만 담은 리스트
value_list = data.values()
print(key_list)
print(value_list)

# 각 키에 따른 값을 하나씩 출력
for key in key_list:
    print(data[key])


### 집합 자료형 ###

'''
중복을 허용하지 않음
순서가 없어 인덱싱을 통해 자료형의 값을 얻을 수 없음
특정 원소가 존재하는지를 검사하는 연산의 시간 복잡도는 O(1)
'''

# 집합 자료형 초기화 방법 1 {1, 2, 3, 4, 5}
data = set([1, 1, 2, 3, 4, 4, 5])
print(data)

# 집합 자료형 초기화 방법 2
data = {1, 1, 2, 3, 4, 4, 5}
print(data)

a = set([1, 2, 3, 4, 5])
b = set([3, 4, 5, 6, 7])

# 합집합 {1, 2, 3, 4, 5, 6, 7}
print(a | b)
# 교집합 {3, 4, 5}
print(a & b)
# 차집합 {1, 2}
print(a - b)

data = set([1, 2, 3])

# 새로운 원소 추가 - 시간 복잡도 O(1)
data.add(4)
print(data)

# 새로운 원소 여러 개 추가
data.update([5, 6])
print(data)

# 특정한 값을 갖는 원소 삭제 - 시간 복잡도 O(1)
data.remove(3)
print(data)