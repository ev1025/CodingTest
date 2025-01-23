def solution(s):
    s = list(s.lower())
    p = [i for i in s if i=='p']
    y = [j for j in s if j=='y']
    
    if len(p) != len(y):
        return False
    else:
        return True
    