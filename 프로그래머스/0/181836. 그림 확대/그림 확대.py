def solution(picture, k):
    answer = []
    for vocab in picture:
        temp = ''.join([j*k for j in vocab])
        for _ in range(k):
            answer.append(temp)
    return answer