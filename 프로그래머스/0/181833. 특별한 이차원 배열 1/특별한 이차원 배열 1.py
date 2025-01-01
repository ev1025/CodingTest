def solution(n):
    answer = [list('0'*n) for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i==j:
                answer[i][j] = 1
            else:
                answer[i][j] = 0
    
    return answer