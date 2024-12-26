def solution(myString):
    answer = ''.join([ i.upper() if i.lower() =='a' else i.lower() for i in myString ])
    return answer