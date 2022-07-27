'''
if 조건문 1:
    조건문 1이 True일 때 실행되는 코드
elif 조건문 2:
    조건문 1에 해당하지 않고, 조건문 2가 True일 때 실행되는 코드
else:
    위의 모든 조건문이 모두 True 값이 아닐 때 실행되는 코드
'''


### 비교 연산자 ###

'''
X == Y
X != Y
X > Y
X < Y
X >= Y
X <= Y
'''


### 논리 연산자 ###

'''
X and Y
X or Y
not X
'''


### 파이썬의 기타 연산자 ###

'''
리스트, 튜플, 문자열, 사전과 같은 자료형 안에 어떠한 값이 존재하는지 확인하는 연산
X in 자료형
X not in 자료형
'''

'''
조건문의 값이 참이라고 해도, 아무것도 처리하고 싶지 않을 때 pass 문을 이용할 수 있음
if score >= 80:
    pass
else:
    print('성적이 80점 미만입니다.')
'''

'''
조건부 표현식을 이용하면 if ~ else문을 한 줄에 작성해 사용할 수 있음
'''

score = 85

if score >= 80: result = "Success"
else: result = "Fail"

# 조건부 표현식
score = 85
result = "Success" if score >= 80 else "Fail"