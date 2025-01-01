def solution(n):
    for i in range(n,n*61):
        if i%6==0 and i%n==0:
            return i//6