def solution(n):
    answer = []
    for num in range(2,n+1):
        temp = []
        if n%num==0:
            for i in range(2,num+1):
                if num%i==0:
                    temp.append(i)
            if len(temp)==1:
                answer.append(num)
    return answer