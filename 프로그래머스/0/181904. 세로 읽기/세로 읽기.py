def solution(my_string, m, c):
    start = 0
    end = m
    new_list = []
    while len(my_string) >= end:
        new_list.append(my_string[start:end])
        start+=m
        end+=m
    return "".join([word[c-1] for word in new_list])