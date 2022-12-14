# 수 찾기
# https://www.acmicpc.net/problem/1920
# 실버 4 | 시간 제한 1초 | 메모리 제한 128MB

'''
N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.
'''

'''
입력 조건
- 첫째 줄에 자연수 N(1 ≤ N ≤ 100,000)이 주어진다.
- 다음 줄에는 N개의 정수 A[1], A[2], …, A[N]이 주어진다.
- 다음 줄에는 M(1 ≤ M ≤ 100,000)이 주어진다.
- 다음 줄에는 M개의 수들이 주어지는데, 이 수들이 A안에 존재하는지 알아내면 된다.
- 모든 정수의 범위는 -231 보다 크거나 같고 231보다 작다.

출력 조건
- M개의 줄에 답을 출력한다. 존재하면 1을, 존재하지 않으면 0을 출력한다.
'''

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return 1
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return 0

n = int(input())
array = list(map(int, input().split()))
array.sort() # 이진 탐색을 이용하기 위해 정렬

m = int(input())
x = list(map(int, input().split()))

for i in x:
    print(binary_search(array, i, 0, n - 1)) # 이진 탐색 이용

# 메모리 46408KB | 시간 552ms | 코드 길이 454B

n = int(input())
array = set(map(int, input().split())) # 집합 자료형 이용

m = int(input())
x = list(map(int, input().split()))

for i in x:
    if i in array:
        print(1)
    else:
        print(0)

# 메모리 49760KB | 시간 192ms | 코드 길이 185B