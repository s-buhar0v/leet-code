def two_sum(nums, target):
    count = len(nums)

    for i in range(0, count):
        for j in range(1, count):
            if i == j:
                continue

            if (nums[i] + nums[j]) == target:
                return [i, j]
