'''
선택 정렬은 가장 작은 데이터를 앞으로 보내는 과정을 N - 1번 반복하는 방법

1. 가장 작은 데이터를 선택하여 맨 앞에 있는 데이터와 바꿈
2. 이후 데이터 중에서 가장 작은 데이터를 선택해서 처리되지 않은 데이터 중 가장 앞에 있는 데이터와 바꿈
3. 마지막 데이터는 가만히 두어도 이미 정렬된 상태이므로 정렬을 마침

선택 정렬의 시간 복잡도 - O(N^2)
'''

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_index = i # 가장 작은 원소의 인덱스
    for j in range(i + 1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i] # 스와프

print(array)