from itertools import permutations

def solution(k, dungeons):
    answer = -1
    
    dungeons_list = []
    for i in range(len(dungeons)):
        if dungeons[i][0] <= k:
            dungeons_list.append(i)
    
    orders = list(permutations(dungeons_list))

    for order in orders:
        temp_k = k
        count = 0
        
        for i in order:
            if dungeons[i][0] > temp_k:
                break
            temp_k -= dungeons[i][1]
            count += 1
        
        if count > answer:
            answer = count
    
    return answer