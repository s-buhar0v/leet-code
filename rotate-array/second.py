# The second solution

def rotate(nums, k):
    result = []
    for i in range(len(nums)):
        result.append(0)

    for index, value in enumerate(nums):
        new_index = (index + k) % len(nums)
        result[new_index] = value

    for i in range(len(result)):
        nums[i] = result[i]
