def solution(my_string):
    answer = sorted([int(i) for i in list(my_string) if 'a'>i])
    return answer