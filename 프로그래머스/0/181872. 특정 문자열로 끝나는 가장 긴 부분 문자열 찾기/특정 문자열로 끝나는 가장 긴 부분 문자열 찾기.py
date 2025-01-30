def solution(myString, pat):
    idx = myString[::-1].index(pat[::-1])
    return myString[:-idx] if myString[:-idx] else myString