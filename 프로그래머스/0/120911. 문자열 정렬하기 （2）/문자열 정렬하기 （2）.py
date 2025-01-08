def solution(my_string):
    my_string = list(my_string.lower())
    my_string.sort(reverse =False)
    return ''.join(my_string)