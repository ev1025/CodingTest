def solution(myString, pat):
    myString = myString.replace("A","TEMP").replace("B","A").replace("TEMP","B")
    return int(pat in myString)