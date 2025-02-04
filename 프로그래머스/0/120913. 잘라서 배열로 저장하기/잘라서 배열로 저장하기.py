def solution(my_str, n):
    answer = []
    start = 0
    end = n
    str_num = len(my_str)
    
    if str_num%n == 0:
        dvide_num = str_num//n
    else:
        dvide_num = str_num//n +1
    
    for _ in range(dvide_num):
        answer.append(my_str[start:end])
        start += n
        end += n
    
    return answer