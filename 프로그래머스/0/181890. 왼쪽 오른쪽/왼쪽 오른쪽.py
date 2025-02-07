def solution(str_list):
    if "l" not in str_list and "r" not in str_list:
        return []
    elif "l" not in str_list and "r" in str_list:
        r_index = str_list.index('r')
        return str_list[r_index+1:]     
    elif "l" in str_list and "r" not in str_list:
        l_index = str_list.index('l')
        return str_list[:l_index] 
    else:
        r_index = str_list.index('r')
        l_index = str_list.index('l')
        if l_index < r_index:
            return str_list[:l_index] 
        else:
            return str_list[r_index+1:]
            