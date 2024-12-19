def solution(my_string, n):
    answer=''
    my_ = [i*n for i in my_string]
    for j in range(len(my_)):
        answer+=my_[j]
    return answer