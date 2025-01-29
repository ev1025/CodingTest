def solution(arr):
    array_count = len(arr)
    div_num = len(arr)
    i = 0
    sq = 2**i

    while div_num%2==0:
        i+=1
        div_num/=2

    while sq < array_count:
        sq*=2

    plus_zero = sq - array_count

    for _ in range(plus_zero):
        arr.append(0)
    
    return arr