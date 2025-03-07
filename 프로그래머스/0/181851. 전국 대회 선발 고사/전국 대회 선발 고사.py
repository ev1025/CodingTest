def solution(rank, attendance):
    temp = {i : index for index, i in enumerate(rank) if attendance[index]}
    sort_temp = sorted(temp.items())
    return sort_temp[0][1]*10000 + sort_temp[1][1]*100 + sort_temp[2][1]