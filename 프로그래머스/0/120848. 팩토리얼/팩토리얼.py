def solution(n):
    i = 1
    for num in range(1,10+1):
        i*=num
        if i>n:
            return num-1
        elif i==n:
            return num
