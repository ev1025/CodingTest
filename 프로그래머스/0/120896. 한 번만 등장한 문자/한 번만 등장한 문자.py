def solution(s):
    return ''.join(sorted(i for i in list(s) if s.count(i)==1))