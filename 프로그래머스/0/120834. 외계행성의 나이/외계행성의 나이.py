def solution(age):
    alpha = list('abcdefghij')
    num_list = [str(i) for i in range(10)]
    dict_val = dict(zip(num_list,alpha))
    return ''.join([dict_val[j] for j in list(str(age))])