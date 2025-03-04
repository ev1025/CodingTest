def solution(spell, dic):
    answer = 0
    dic = [sorted(j) for j in dic]
    spell = sorted(spell)
    print(f'spell:{spell}')
    for i in dic:
        print(i)
        if spell == i:
            
            return 1
    if answer == 0:
        return 2
        
    return answer