def solution(strArr):
    num_list = [len(i) for i in strArr]
    num_dict = {}
    for i in num_list:
        if i not in num_dict.keys():
            num_dict[i] = 1
        else:
            num_dict[i]+=1

    return sorted(num_dict.items(), key= lambda x: x[1], reverse=True)[0][1]