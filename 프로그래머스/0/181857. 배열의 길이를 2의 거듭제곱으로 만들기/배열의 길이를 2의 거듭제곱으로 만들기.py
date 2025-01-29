def solution(arr):
    array_num = len(arr)
    i = 0

    while 2**i < array_num:
        i+=1

    return arr + [0] *(2**i - array_num)