def find_disappeared_numbers(numbers):
    for i in range(0, len(numbers)):
        current_abs = abs(numbers[i])
        numbers[current_abs-1] = -abs(numbers[current_abs-1])

    result = []
    for i, v in enumerate(numbers):
        if v > 0:
            result.append(i+1)

    return result
