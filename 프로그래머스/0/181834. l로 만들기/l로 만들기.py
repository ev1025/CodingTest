def solution(myString):
    change = {'l': ['a','b','c','d','e','f','g','h','i','j','k']}
    answer =''.join([ "l" if i in change['l'] else i for i in myString ])
    return answer