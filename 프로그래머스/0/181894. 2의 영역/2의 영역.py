def solution(arr):
    idx_list = [idx for idx, val in enumerate(arr) if val ==2]
    if len(idx_list) >=2:
        return arr[idx_list[0]:idx_list[-1]+1]
    else:
        if len(idx_list):
            return [2]
        else:
            return [-1]
