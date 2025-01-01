def solution(my_string, num1, num2):
    new_str = ''
    for i in my_string:
        if my_string.index(i) == num1:
            new_str+= my_string[num2]
        elif my_string.index(i)==num2:
            new_str+= my_string[num1]
        else:
            new_str+=i
    return new_str