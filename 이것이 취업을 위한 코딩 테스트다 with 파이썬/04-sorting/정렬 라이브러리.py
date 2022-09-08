'''
파이썬은 기본 정렬 라이브러리인 sorted() 함수 제공
sorted()는 퀵 정렬과 동작 방식이 비슷한 병합 정렬을 기반으로 만들어졌는데,
병합 정렬은 일반적으로 퀵 정렬보다 느리지만 최악의 경우에도 시간 복잡도 O(NlogN)을 보장
리스트, 딕셔너리 자료형 등을 입력받아서 정렬된 결과를 출력하며,
집합 자료형이나 딕셔너리 자료형을 입력받아도 반환되는 결과는 리스트 자료형

리스트 객체의 내장 함수인 sort()를 이용하면 별도의 정렬된 리스트가 반환되지 않고 내부 원소가 바로 정렬됨

sorted(), sort()의 key 값으로는 하나의 함수 또는 람다 함수가 들어가야 하며, 이는 정렬 기준이 됨

정렬 라이브러리는 항상 최악의 경우에도 시간 복잡도 O(NlogN)을 보장
'''

# sorted()
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

result = sorted(array)
print(result)

# sort()
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

array.sort()
print(array)

# key 활용
array = [('바나나', 2), ('사과', 5), ('당근', 3)]

def setting(data):
    return data[1]

result = sorted(array, key=setting)
print(result)