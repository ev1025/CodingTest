def solution(array):
    array.sort()
    num = int(len(array)/2+0.5)
    answer= array[num-1]
    return answer