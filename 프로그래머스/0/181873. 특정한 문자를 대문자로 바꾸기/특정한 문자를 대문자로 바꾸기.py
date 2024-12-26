def solution(my_string, alp):
    answer = ''
    answer = ''.join([answer + i.upper() if i == alp else answer+i for i in my_string ])
    return answer