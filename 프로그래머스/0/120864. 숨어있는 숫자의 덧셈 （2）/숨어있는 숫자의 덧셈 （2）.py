def solution(my_string):
    answer=0
    strings = ''.join([num if num.isdigit() else 'a' for num in list(my_string)])
    strings = strings.split('a')
    for i in strings:
        if i !='':
            answer+=int(i)
    return answer
