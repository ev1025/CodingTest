def solution(n, k):
    answer = [i for i in list(range(1,n+1)) if i%k==0]
    return answer