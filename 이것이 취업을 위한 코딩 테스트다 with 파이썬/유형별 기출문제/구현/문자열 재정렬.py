# 문자열 재정렬
# 난이도 하 | 풀이 시간 20분 | 시간 제한 1초 | 메모리 제한 128MB

'''
알파벳 대문자와 숫자(0 ~ 9)로만 구성된 문자열이 입력으로 주어집니다.
이때 모든 알파벳을 오름차순으로 정렬하여 이어서 출력한 뒤에, 그 뒤에 모든 숫자를 더한 값을 이어서 출력합니다.

예를 들어 KIKA5CB7이라는 값이 들어오면 ABCKK13을 출력합니다.
'''

'''
입력 조건
- 첫째 줄에 하나의 문자열 S가 주어집니다. (1 <= S의 길이 <= 10,000)

출력 조건
- 첫째 줄에 문제에서 요구하는 정답을 출력합니다.
'''

s = input()

num = 0
alphabets = []
check = False

for i in s:
    # if "A" <= s[i] <= "Z":
    if i.isalpha():
        alphabets.append(i)
    else:
        num += int(i)
        check = True

alphabets.sort()
for alphabet in alphabets:
    print(alphabet, end='')
if check: # 숫자가 하나라도 존재하는 경우 출력
    print(num)