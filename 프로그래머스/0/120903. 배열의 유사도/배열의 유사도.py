def solution(s1, s2):
    answer = 0
    a = sum([answer+1 for i in s1 if i in s2])
    return a
