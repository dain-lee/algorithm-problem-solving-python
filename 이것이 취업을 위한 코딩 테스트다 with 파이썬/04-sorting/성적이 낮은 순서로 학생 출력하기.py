# 성적이 낮은 순서로 학생 출력하기
# 난이도 하 | 풀이 시간 20분 | 시간 제한 1초 | 메모리 제한 128MB | 기출 D 기업 프로그래밍 콘테스트 예선

'''
N명의 학생 정보가 있다.
학생 정보는 학생의 이름과 학생의 성적으로 구분된다.
각 학생의 이름과 성적 정보가 주어졌을 때 성적이 낮은 순서대로 학생의 이름을 출력하는 프로그램을 작성하시오.
'''

'''
입력 조건
- 첫 번째 줄에 학생의 수 N이 입력된다. (1 <= N <= 100,000)
- 두 번째 줄부터 N + 1번째 줄에는 학생의 이름을 나타내는 문자열 A와 학생의 성적을 나타내는 정수 B가 공백으로 구분되어 입력된다.
- 문자열 A의 길이와 학생의 성적은 100이하의 자연수이다.

출력 조건
- 모든 학생의 이름을 성적이 낮은 순서대로 출력한다. 성적이 동일한 학생들의 순서는 자유롭게 출력해도 괜찮다.
'''

# N을 입력받기
n = int(input())

# N명의 학생 정보를 입력받아 리스트에 저장
# array = [tuple(input().split()) for _ in range(n)]
array = []
for i in range(n):
    input_data = input().split()
    # 이름은 문자열 그대로, 점수는 정수형으로 변환하여 저장
    array.append((input_data[0], int(input_data[1])))

# 키(Key)를 이용하여, 점수를 기준으로 정렬
# array = sorted(array, key=lambda student:student[1])
array.sort(key=lambda x:x[1])

# 정렬이 수행된 결과를 출력
for student in array:
    print(student[0], end=' ')