def move(nums):
    left = 0
    for i, v in enumerate(nums):
        if v != 0:
            nums[left], nums[i] = nums[i], nums[left]
            left += 1
