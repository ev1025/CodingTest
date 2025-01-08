def solution(num, k):
    answer = 0
    return str(num).index(str(k)) + 1 if str(k) in str(num) else -1