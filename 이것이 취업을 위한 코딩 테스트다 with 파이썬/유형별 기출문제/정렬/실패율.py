# 실패율
# 난이도 하 | 풀이 시간 20분 | 시간 제한 1초 | 메모리 제한 128MB
# https://school.programmers.co.kr/learn/courses/30/lessons/42889

'''
슈퍼 게임 개발자 오렐리는 큰 고민에 빠졌습니다.
그녀가 만든 프랜즈 오천성이 대성공을 거뒀지만, 요즘 신규 사용자의 수가 급감했습니다.
원인은 신규 사용자와 기존 사용자 사이에 스테이지 차이가 너무 큰 것이 문제였습니다.
이 문제를 어떻게 할까 고민 한 그녀는 동적으로 게임 시간을 늘려서 난이도를 조절하기로 했습니다. 
역시 슈퍼 개발자라 대부분의 로직은 쉽게 구현했지만, 실패율을 구하는 부분에서 위기에 빠지고 말았습니다.
오렐리를 위해 실패율을 구하는 코드를 완성하세요.

실패율은 다음과 같이 정의합니다.
- 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수
전체 스테이지의 개수 N, 게임을 이용하는 사용자가 현재 멈춰있는 스테이지의 번호가 담긴 배열 stages가 매개변수로 주어질 때,
실패율이 높은 스테이지부터 내림차순으로 스테이지의 번호가 담겨있는 배열을 return 하도록 solution 함수를 완성하세요.
'''

'''
제한 사항
- 스테이지의 개수 N은 1 이상 500 이하의 자연수입니다.
- stages의 길이는 1 이상 200,000 이하입니다.
- stages에는 1 이상 N + 1 이하의 자연수가 담겨있습니다.
- 각 자연수는 사용자가 현재 도전 중인 스테이지의 번호를 나타냅니다.
- 단, N + 1 은 마지막 스테이지(N 번째 스테이지) 까지 클리어 한 사용자를 나타냅니다.
- 만약 실패율이 같은 스테이지가 있다면 작은 번호의 스테이지가 먼저 오도록 하면 됩니다.
- 스테이지에 도달한 유저가 없는 경우 해당 스테이지의 실패율은 0으로 정의합니다.
'''

def solution(N, stages):
    data = [0] * (N + 2) # 각 스테이지에서 머물러 있는 사람 수 배열
    for s in stages:
        data[s] += 1
    
    for i in range(len(data)-2, 0, -1): # 마지막 스테이지부터 돌면서, 현재 스테이지에 도달한 플레이어 수 = 현재 스테이지에서 머물러 있는 사람 수 + 다음 스테이지에 도달한 플레이어 수
        data[i] += data[i + 1]
    
    result = []
    for i in range(1, len(data)-1):
        # 실패율 계산 (나눗셈 연산의 경우 분모가 변수일 때 꼭 0이 아닌지 확인 !!)
        if data[i] != 0:
            result.append(((data[i] - data[i+1])/data[i] , i))
        # 도달한 사람이 없는 경우
        else:
            result.append((0, i))
    # 실패율 내림차순, 스테이지 번호 오름차순으로 정렬
    result.sort(key= lambda x:(-x[0], x[1]))
    
    answer = []
    for i in result:
        answer.append(i[1])
    
    return answer


def solution(N, stages):
    answer = []
    length = len(stages) # 전체 플레이어 수

    # 스테이지 번호를 1부터 N까지 증가시키며
    for i in range(1, N + 1):
        # 해당 스테이지에 머물러 있는 사람의 수 계산
        count = stages.count(i)

        # 실패율 계산
        if length == 0: # 도달한 플레이어가 없으면
            fail = 0
        else:
            fail = count / length

        # 리스트에 (스테이지 번호, 실패율) 원소 삽입
        answer.append((i, fail))
        length -= count # 다음 스테이지에 도달한 플레이어 수 = 현재 스테이지에 도달한 플레이어 수 - 현재 스테이지에 머물러 있는 플레이어 수

    # 실패율을 기준으로 각 스테이지를 내림차순 정렬
    answer = sorted(answer, key=lambda t: t[1], reverse=True)

    # 정렬된 스테이지 번호 출력
    answer = [i[0] for i in answer]
    return answer