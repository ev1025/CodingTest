def solution(q, r, code):
    answer = ''.join([code[val] for val in range(len(code)) if val%q==r])
            
    return answer