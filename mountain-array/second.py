def peak_index(arr):
    left = 0
    right = len(arr) - 1
    result = -1

    while left < right:
        mid = (left + right) // 2

        if arr[mid] > arr[mid+1]:
            result = mid
            right = mid
        else:
            result = mid + 1
            left = mid + 1

    return result
