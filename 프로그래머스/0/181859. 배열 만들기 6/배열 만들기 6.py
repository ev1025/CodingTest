def solution(arr):
    i = 0
    skt = []
    while i <len(arr):
        if skt ==[]:
            skt.append(arr[i])
            i+=1
        elif skt[-1] == arr[i]:
            skt.pop()
            i+=1
        elif skt[-1] != arr[i]:
            skt.append(arr[i])
            i+=1
    return skt if skt else [-1]
            
        
    answer = []
    return answer