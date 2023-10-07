import math

def solution(progresses, speeds):
    answer = []
    deploy = []
    
    for i in range(len(progresses)):
        feature = progresses[i]
        speed = speeds[i]    
        deploy.append(math.ceil((100 - feature) / speed))
    
    count = 1
    temp = deploy[0]
    for i in range(1, len(deploy)):
        if temp >= deploy[i]:
            count += 1
        else:
            answer.append(count)
            count = 1
            temp = deploy[i]
    answer.append(count)
    
    return answer