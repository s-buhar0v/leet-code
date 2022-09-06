def move(nums):
    zeros = []
    others = []

    for num in nums:
        if num == 0:
            zeros.append(num)
        else:
            others.append(num)

    for i, v in enumerate(others + zeros):
        nums[i] = v
