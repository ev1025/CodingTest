def solution(numbers):
    str_num = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    real_num = [str(i) for i in range(0,10)]
    for k, v in dict(zip(str_num, real_num)).items():
        if k in numbers:
            numbers = numbers.replace(k,v)
    return int(numbers)