# 정렬된 배열에서 특정 수의 개수 구하기
# 난이도 중 | 풀이 시간 30분 | 시간 제한 1초 | 메모리 제한 128MB

'''
N개의 원소를 포함하고 있는 수열이 오름차순으로 정렬되어 있습니다.
이때 이 수열에서 x가 등장하는 횟수를 계산하세요.
예를 들어 수열 {1, 1, 2, 2, 2, 2, 3}이 있을 때 x = 2라면, 현재 수열에서 값이 2인 원소가 4개이므로 4를 출력합니다.
단, 이 문제는 시간 복잡도 O(logN)으로 알고리즘을 설계하지 않으면 '시간 초과'판정을 받습니다.
'''

'''
입력 조건
- 첫째 줄에 N과 x가 정수 형태로 공백으로 구분되어 입력됩니다. (1 <= N <= 1,000,000), (-10^9 <= x <= 10^9)
- 둘째 줄에 N개의 원소가 정수 형태로 공백으로 구분되어 입력됩니다. (-10^9 <= 각 원소의 값 <= 10^9)

출력 조건
- 수열의 원소 중에서 값이 x인 원소의 개수를 출력합니다. 단, 값이 x인 원소가 하나도 없다면 -1을 출력합니다.
'''

'''
x가 처음 등장하는 인덱스와 x가 마지막으로 등장하는 인덱스를 각각 계산한 뒤에, 그 인덱스의 차이를 계산하여 문제 해결
O(logN)안에 찾아내기 위해 이진 탐색 활용
'''

# 처음 위치를 찾는 이진 탐색 메서드
def first(array, target, start, end):
    if start > end:
        return None
    mid = (start + end // 2)
    # 해당 값을 가지는 원소 중에서 가장 왼쪽에 있는 경우에만 인덱스 반환
    if (mid == 0 or target > array[mid - 1]) and array[mid] == target: # mid == 0일 경우 mid - 1은 인덱스 에러이기 때문에 조건 추가
        return mid
    # 중간점의 값 보다 찾고자 하는 값이 작거나 같은 경우 왼쪽 확인
    elif array[mid] >= target:
        return first(array, target, start, mid - 1)
    # 중간점의 값 보다 찾고자 하는 값이 큰 경우 오른쪽 확인
    else:
        return first(array, target, mid + 1, end)

# 마지막 위치를 찾는 이진 탐색 메서드
def last(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    # 해당 값을 가지는 원소 중에서 가장 오른쪽에 있는 경우에만 인덱스 반환
    if (mid == n - 1 or target < array[mid + 1]) and array[mid] == target:
        return mid
    # 중간점의 값 보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    elif array[mid] > target:
        return last(array, target, start, mid - 1)
    # 중간점의 값 보다 찾고자 하는 값이 크거나 같은 경우 오른쪽 확인
    else:
        return last(array, target, mid + 1, end)

n, x = map(int, input().split())
array = list(map(int, input().split()))

left = first(array, x, 0, len(array) - 1)

if left == None:
    print(-1)
    exit(0)

right = last(array, x, 0, len(array) - 1)

print(right - left + 1)


# bisect 라이브러리 활용
from bisect import bisect_left, bisect_right

n, x = map(int, input().split())
data = list(map(int, input().split()))

left = bisect_left(data, x)
right = bisect_right(data, x)

result = right - left
if result:
    print(result)
else:
    print(-1)