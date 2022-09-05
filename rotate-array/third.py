# The third solution

def reverse(nums, begin, end):
    while begin < end:
        nums[begin], nums[end] = nums[end], nums[begin]

        begin += 1
        end -= 1


def rotate(nums, k):
    nums_length = len(nums)
    k = k % nums_length

    begin, end = 0, nums_length - 1
    reverse(nums, begin, end)

    begin, end = 0, k - 1
    reverse(nums, begin, end)

    begin, end = k, nums_length - 1
    reverse(nums, begin, end)
