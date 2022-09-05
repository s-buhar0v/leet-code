# The first solution

def rotate(nums, k):
    nums_count = len(nums)

    if k == 0 or (nums_count == 2 and k % 2 == 0):
        return

    nums_for_rotation = nums[nums_count - k:nums_count]
    other_nums = nums[:nums_count - k]

    result = []

    if len(nums) == 2:
        result = [nums[1], nums[0]]

        for i in range(nums_count):
            nums[i] = result[i]

        return

    for i in nums_for_rotation:
        result.append(i)

    result = result + other_nums

    for i in range(len(result)):
        nums[i] = result[i]
