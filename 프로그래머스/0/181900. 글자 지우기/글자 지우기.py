def solution(my_string, indices):
    num_list = [i for i in range(len(my_string)) if i not in indices]
    return ''.join(my_string[j] for j in num_list)