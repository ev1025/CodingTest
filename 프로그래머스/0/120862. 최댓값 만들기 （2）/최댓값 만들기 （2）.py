def solution(numbers):
    numbers.sort()
    answer = (numbers[0] * numbers[1], numbers[-1]*numbers[-2])
    return max(answer)