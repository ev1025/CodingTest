def solution(n):
    st = n**(1/2)
    if st*st == n and st%1 == 0:
        return (st+1)**2
    else:
        return -1