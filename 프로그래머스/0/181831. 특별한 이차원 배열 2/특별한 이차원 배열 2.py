def solution(arr):
    sum_list = sum([1 for j in range(len(arr)) for i in range(len(arr)) if arr[i][j] == arr[j][i]])     
    return  1 if sum_list == len(arr)**2 else 0