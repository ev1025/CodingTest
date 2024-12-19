def solution(n, k):
    sheep = 12000
    drink = 2000
    
    if n//10 !=0:
        k -= n//10
        
    answer = n*sheep + k*drink
    return answer