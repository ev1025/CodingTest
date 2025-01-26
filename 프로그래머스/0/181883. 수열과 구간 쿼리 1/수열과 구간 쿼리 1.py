def solution(arr, queries):
    for s,e in queries:
        for num in range(s,e+1):
            arr[num]+=1 
    return arr