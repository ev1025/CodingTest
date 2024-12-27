def solution(arr):
    temp = []
    for i in arr:
        if (i >=50)&(i%2 == 0):
            temp.append(i/2)
        elif (i<50)&(i%2 !=0):
            temp.append(i*2)
        else:
            temp.append(i)
    return temp