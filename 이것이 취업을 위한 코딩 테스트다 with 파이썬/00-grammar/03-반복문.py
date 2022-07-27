### while문 ###

i = 1
result = 0

# i가 9보다 작거나 같을 때 아래 코드를 반복적으로 실행
while i <= 9:
    if i % 2 == 1:
        result += i
    i += 1

print(result)


### for문 ###

result = 0

# i는 1부터 9까지의 모든 값을 순회
for i in range(1, 10):
    result += i

print(result)

'''
반복문 안에서 continue를 만나면 프로그램의 흐름은 반복문의 처음으로 돌아감
'''