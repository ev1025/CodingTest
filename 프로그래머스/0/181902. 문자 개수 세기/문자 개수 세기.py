def solution(my_string):
    letters_list = [chr(i) for i in range(65, 91)] + [chr(i) for i in range(97, 123)] 
    answer = [ 0 if i not in my_string else my_string.count(i) for i in letters_list]
    
    return answer