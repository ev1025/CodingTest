def solution(sides):
    max_num = max(sides[0],sides[1], sides[2])
    sides.remove(max_num)
    if max_num < sum(sides):
        answer = 1
    else:
        answer = 2
    return answer