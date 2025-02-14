def solution(numbers, k):
    j = (k-1)*2
    if len(numbers) <j:
        while len(numbers)<j:
             j-= len(numbers)
        return numbers[j]
    return numbers[(k-1)*2]