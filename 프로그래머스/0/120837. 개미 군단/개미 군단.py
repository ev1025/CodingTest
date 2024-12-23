def solution(hp):
    answer = 0
    temp = [5,3,1]
    for i in temp:
        answer += hp//i
        hp %= i
    return answer