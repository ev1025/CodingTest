def solution(bin1, bin2):
    sum_int = int(bin1)+int(bin2)
    while '2' in str(sum_int): 
        sum_len = len(str(sum_int))
        for i in str(sum_int):   
            if i == '2':
                sum_int += 10**(sum_len)
                sum_int -= 2*(10**(sum_len-1))
                sum_int
            sum_len-=1
    return str(sum_int)