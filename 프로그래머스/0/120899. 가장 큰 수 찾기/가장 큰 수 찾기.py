def solution(array):
    a = sorted(array)
    answer = [i for i in range(len(a)) if array[i] == a[-1]]
    answer.insert(0,a[-1])
    return answer