def solution(numbers, direction):
    numbers.insert(0, numbers.pop(-1)) if direction == 'right' else numbers.insert(len(numbers),numbers.pop(0))
    return numbers