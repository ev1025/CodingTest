def solution(num_list):
    a = 1
    for i in num_list:
        if len(num_list) > 10:
            return sum(num_list)
        a*=i
    return a