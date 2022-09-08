'''
퀵 정렬은 기준을 설정한 다음 큰 수와 작은 수를 교환한 후 리스트를 반으로 나누는 방식으로 동작

퀵 정렬에서는 큰 숫자와 작은 숫자를 교환할 때, 교환하기 위핸 '기준'인 피벗을 사용
퀵 정렬을 수행하기 전에는 피벗을 어떻게 설정할 것인지 미리 명시해야 함

호어 분할 방식 - 리스트에서 첫 번째 데이터를 피벗으로 정함

퀵 정렬은 재귀 함수 형태로 작성
끝나는 조건은 현재 리스트의 데이터 개수가 1개인 경우

1. 첫 번째 데이터를 피벗으로 설정
2. 두 번째 데이터 부터 시작하여 피벗보다 큰 데이터를 찾음
3. 마지막 데이터 부터 시작하여 피벗보다 작은 데이터를 찾음
4. 그 결과 두 인덱스가 엇갈렸다면 작은 데이터와 피벗을 교체, 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
5. 피벗 이동 후 왼쪽 부분과 오른쪽 부분에 각각 퀵 정렬 수행
6. 윈소가 1개인 경우 종료

퀵 정렬의 시간 복잡도 - O(NlogN), 최악의 경우 O(N^2)
리스트의 가장 왼쪽 데이터를 피벗으로 삼을 때, '이미 데이터가 정렬되어 있는 경우'에는 매우 느리게 동작
'''

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    if start >= end: # 원소가 1개인 경우 종료
        return
    pivot = start # 피벗은 첫 번째 원소
    left = start + 1
    right = end
    while left <= right:
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while left <= end and array[left] <= array[pivot]:
            left += 1
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left > right: # 엇갈렸다면 작은 데이터와 피벗을 교체
            array[right], array[pivot] = array[pivot], array[right]
        else: # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            array[left], array[right] = array[right], array[left]
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)

quick_sort(array, 0, len(array) - 1)
print(array)

# 피벗과 데이터를 비교하는 비교 연산 횟수가 증가하므로 시간 면에서는 조금 비효율적이지만, 더 직관적이고 기억하기 쉬운 코드
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array):
    # 리스트가 하나 이하의 원소만을 담고 있다면 종료
    if len(array) <= 1:
        return array

    pivot = array[0] # 피벗은 첫 번째 원소
    tail = array[1:] # 피벗을 제외한 리스트

    left_side = [x for x in tail if x <= pivot] # 분할된 왼쪽 부분
    right_side = [x for x in tail if x > pivot] # 분할된 오른쪽 부분

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행하고, 전체 리스트를 반환
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))