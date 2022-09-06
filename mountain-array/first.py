def peak_index(arr):
    max = 0
    max_index = -1

    for i, v in enumerate(arr):
        if i == 0 or i == len(arr) - 1:
            continue
        if v > max and v > arr[i-1] and v > arr[i+1]:
            max = v
            max_index = i

    return max_index
