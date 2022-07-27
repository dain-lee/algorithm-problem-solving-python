'''
list(map(int, input().split()))
먼저 input()으로 입력받은 문자열을 split()을 이용해 공백으로 나눈 리스트로 바꾼 뒤에,
map을 이용하여 해당 리스트의 모든 원소에 int()함수를 적용
최종적으로 그 결과를 list()로 다시 바꿈으로써 입력받은 문자열을 띄어쓰기로 구분하여 각각 숫자 자료형으로 저장
'''

# 데이터의 개수 입력
n = int(input())
# 각 데이터를 공백으로 구분하여 입력
data = list(map(int, input().split()))

data.sort(reverse = True)
print(data)

# n, m, k를 공백으로 구분하여 입력
n, m, k = map(int, input().split())

print(n, m, k)

'''
파이썬의 기본 input() 함수는 동작 속도가 느려서 시간 초과로 오답 판정을 받을 수 있기 때문에
입력의 개수가 많은 경우에는 단순히 input() 함수를 그대로 사용하지 않음
이 경우 파이썬의 sys 라이브러리에 정의되어 있는 sys.stdin.readline() 함수 이용
sys 라이브러리를 사용할 때는 한 줄 입력을 받고 나서 rstrip() 함수를 꼭 호출해야 함
readline()으로 입력하면 입력 후 엔터가 줄 바꿈 기호로 입력되는데, 이 공백 문자를 제거하려면 rstrip() 함수를 사용해야 함
'''

import sys

# 문자열 입력받기
data = sys.stdin.readline.rstrip()
print(data)

'''
print()는 각 변수를 콤마(,)로 구분하여 매개변수로 넣을 수 있는데, 이 경우 각 변수가 띄어쓰기로 구분되어 출력
'''

'''
문자열과 수를 함께 출력해야 하는 경우 단순히 더하기 연산자를 이용하여 문자열과 수를 더하면 오류가 발생
str() 함수를 이용하여 출력하고자 하는 변수 데이터를 문자열로 바꾸어주거나,
혹은 각 자료형을 콤마(,)를 기준으로 구분하여 출력
'''

# 변수를 문자열로 바꾸어 출력
answer = 7

print("정답은 " + str(answer) + "입니다.")

# 각 변수를 콤마로 구분하여 출력
answer = 7

print("정답은", answer, "입니다.")

'''
f-string은 문자열 앞에 접두사 'f'를 붙임으로써 사용할 수 있는데,
f-string을 이용하면 단순히 중괄호 안에 변수를 넣음으로써, 자료형의 변환 없이도 간단히 문자열과 정수를 함께 넣을 수 있음
'''

answer = 7
print(f"정답은 {answer}입니다.")