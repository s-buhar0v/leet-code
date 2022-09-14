def longest_sequence(numbers):
    result = []
    for i in range(0, len(numbers)):
        result.append(1)

    for i in range(1, len(numbers)):
        for j in range(0, i):
            if numbers[j] < numbers[i]:
                result[i] = max(result[i], result[j]+1)

    return max(result)
