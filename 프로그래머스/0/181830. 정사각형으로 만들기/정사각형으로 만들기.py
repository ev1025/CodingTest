def solution(arr):
    row = len(arr)
    col = len(arr[0])
    
    if row > col:
        minus = row-col
        for i in arr:
            for _ in range(minus):
                i.append(0)
    elif row < col:
        for _ in range(col-row):
            arr.append([0]*col )
    else:
        return arr
    return arr