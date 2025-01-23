def solution(n):
    answer = list(str(n))
    abc = [int(answer.pop()) for _ in range(len(answer))]
    return abc