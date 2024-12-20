def solution(array, height):
    answer = [1 for i in array if height < i] 
    return sum(answer)