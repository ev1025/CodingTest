def solution(arr, k):
    answer = []
    for i in arr:
        if i not in answer:
            answer.append(i)
    if len(answer) <k:     
        while len(answer) != k:
            answer.append(-1)
    else:
        answer = answer[:k]
    return answer 