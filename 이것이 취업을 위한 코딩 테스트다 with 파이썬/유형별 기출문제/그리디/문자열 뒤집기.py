# 문자열 뒤집기
# 난이도 하 | 풀이 시간 20분 | 시간 제한 2초 | 메모리 제한 128MB

'''
다솜이는 0과 1로만 이루어진 문자열 S를 가지고 있습니다.
다솜이는 이 문자열 S에 있는 모든 숫자를 전부 같게 만들려고 합니다.
다솜이가 할 수 있는 행동은 S에서 연속된 하나 이상의 숫자를 잡고 모두 뒤집는 것입니다.
뒤집는 것은 1을 0으로, 0을 1로 바꾸는 것을 의미합니다.

예를 들어 S = 0001100일 때는 다음과 같습니다.
1. 전체를 뒤집으면 1110011이 됩니다.
2. 4번째 문자부터 5번째 문자까지 뒤집으면 1111111이 되어서 두 번 만에 모두 같은 숫자로 만들 수 있습니다.

하지만, 처음부터 4번째 문자부터 5번째 문자까지 문자를 뒤집으면 한 번에 0000000이 되어서 1번 만에 모두 같은 숫자로 만들 수 있습니다.
문자열 S가 주어졌을 때, 다솜이가 해야 하는 행동의 최소 횟수를 출력하세요.
'''

'''
입력 조건
- 첫째 줄에 0과 1로만 이루어진 문자열 S가 주어집니다. S의 길이는 100만보다 작습니다.

출력 조건
- 첫째 줄에 다솜이가 해야 하는 행동의 최소 횟수를 출력합니다.
'''

'''
전부 0으로 바꾸는 경우와 전부 1로 바꾸는 경우 중에서 더 적은 횟수를 가지는 경우를 계산
0001100의 경우 전부 0으로 바꾸려면 1번('11' 뒤집기), 전부 1로 바꾸려면 2번('000', '00' 뒤집기) 

문자열에서 하나 이상의 연속된 0 묶음과 1 묶음의 수를 계산해서 작은 수 출력
'''

s = list(map(int, input()))
result = [0, 0]
result[s[0]] += 1 # 첫 번째 원소 묶음 처리

for i in range(1, len(s)):
    if s[i] != s[i - 1]: # 이전 수와 현재 수가 다르면 현재 수 묶음에 +1
        result[s[i]] += 1

print(min(result))