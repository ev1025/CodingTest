def solution(arr, queries):
    answer = []
    for s,e,k in queries:            
        temp = [arr[i] for i in range(s,e+1) if arr[i] >k]
        if temp == []:
            answer.append(-1)
        else:
            answer.append(min(temp))
    return answer