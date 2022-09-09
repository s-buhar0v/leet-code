import re


def is_perfect_square(num):
    if num == 1:
        return True

    left = 1
    right = num - 1

    while left <= right:
        mid = (left + right) // 2

        square = mid * mid

        if square == num:
            return True

        if num < square:
            right = mid - 1
        else:
            left = mid + 1

    return False