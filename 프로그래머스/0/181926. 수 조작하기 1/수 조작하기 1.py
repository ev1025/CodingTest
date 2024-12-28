def solution(n, control):
    dict_n = {'w':1,
             's':-1,
             'd':10,
             'a':-10}
    for i in control:
         n += dict_n[i]
    
    return n