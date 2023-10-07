from collections import deque

def solution(begin, target, words):
    
    if target not in words:
        return 0
    
    def bfs():
        queue = deque([])
        for word in words:
            if compare_alpha(begin, word):
                queue.append((word, 1))
        
        while queue:
            current_word, count = queue.popleft()
            if current_word == target:
                return count
            
            for word in words:
                if compare_alpha(current_word, word):
                    queue.append((word, count + 1))
        
        return 0
            
        
    def compare_alpha(begin, word):
        flag = False
        for i in range(len(word)):
            if begin[i] != word[i]:
                if flag:
                    return False
                flag = True
        return flag
    
    return bfs()