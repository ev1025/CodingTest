def solution(emergency):
    answer = sorted(emergency, reverse=True)
    for idx, value in enumerate(emergency):
        emergency[idx] = answer.index(value)+1
    return emergency