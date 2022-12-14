# 단어 정렬
#
# 실버 5 | 시간 제한 2초 | 메모리 제한 256MB

'''
알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.
1. 길이가 짧은 것부터
2. 길이가 같으면 사전 순으로
'''

'''
입력 조건
- 첫째 줄에 단어의 개수 N이 주어진다. (1 ≤ N ≤ 20,000)
- 둘째 줄부터 N개의 줄에 걸쳐 알파벳 소문자로 이루어진 단어가 한 줄에 하나씩 주어진다.
- 주어지는 문자열의 길이는 50을 넘지 않는다.

출력 조건
- 조건에 따라 정렬하여 단어들을 출력한다. 단, 같은 단어가 여러 번 입력된 경우에는 한 번씩만 출력한다.
'''

import sys
input = sys.stdin.readline

n = int(input())
words = list(set([input().rstrip() for _ in range(n)])) # 단어 중복을 없애기 위해 집합 자료형으로 변환 후 다시 리스트로 변환
words.sort(key=lambda x:(len(x), x)) # 길이로 정렬한 후 길이가 같으면 사전 순으로 정렬
print(*words, sep='\n')

# 메모리 35452KB | 시간 108ms | 코드 길이 172B