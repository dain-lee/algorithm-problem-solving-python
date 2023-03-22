# 친구 네트워크
# https://www.acmicpc.net/problem/4195
# 골드 2 | 시간 제한 3초 | 메모리 제한 256MB

'''
민혁이는 소셜 네트워크 사이트에서 친구를 만드는 것을 좋아하는 친구이다.
우표를 모으는 취미가 있듯이, 민혁이는 소셜 네트워크 사이트에서 친구를 모으는 것이 취미이다.

어떤 사이트의 친구 관계가 생긴 순서대로 주어졌을 때, 두 사람의 친구 네트워크에 몇 명이 있는지 구하는 프로그램을 작성하시오.

친구 네트워크란 친구 관계만으로 이동할 수 있는 사이를 말한다.
'''

'''
입력 조건
- 첫째 줄에 테스트 케이스의 개수가 주어진다.
- 각 테스트 케이스의 첫째 줄에는 친구 관계의 수 F가 주어지며, 이 값은 100,000을 넘지 않는다.
- 다음 F개의 줄에는 친구 관계가 생긴 순서대로 주어진다.
- 친구 관계는 두 사용자의 아이디로 이루어져 있으며, 알파벳 대문자 또는 소문자로만 이루어진 길이 20 이하의 문자열이다.

출력 조건
- 친구 관계가 생길 때마다, 두 사람의 친구 네트워크에 몇 명이 있는지 구하는 프로그램을 작성하시오.
'''

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a != b: # 루트 노드가 같다면 이미 연결되어 있는 것, 대소 비교 필요 없음
        parent[b] = a
        count[a] += count[b]

    return count[a]

t = int(input())
for _ in range(t):
    f = int(input())
    parent = {} # 문자를 그대로 저장, not in 연산을 빠르게 하기 위해 딕셔너리 사용
    count = {} # key = 이름, value = count
    index_num = 0

    for _ in range(f):
        a, b = input().split()
        if a not in parent:
            parent[a] = a
            count[a] = 1
        if b not in parent:
            parent[b] = b
            count[b] = 1

        print(union_parent(parent, a, b))

# 메모리 61296KB | 시간 288ms | 코드 길이 735B