def solution(seoul):
    index_num = [i for i in range(len(seoul)) if seoul[i]=='Kim']
    return f'김서방은 {index_num[0]}에 있다'