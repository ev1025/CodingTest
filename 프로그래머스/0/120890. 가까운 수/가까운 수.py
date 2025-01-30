def solution(array, n):
    minus_list = [abs(n-num) for num in array]
    min_value = min(minus_list)
    x = dict(zip(array,minus_list))
    min_keys = [key for key,value in x.items() if value == min_value]
    
    return min(min_keys)
