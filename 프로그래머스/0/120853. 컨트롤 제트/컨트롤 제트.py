def solution(s):
    s= s.split()
    idx_list = [idx for idx, val in enumerate(s) if val=="Z"]
    for i in idx_list:
        s[i] = -int(s[i-1])
    s = list(map(int,s))
    
            
    return sum(s)