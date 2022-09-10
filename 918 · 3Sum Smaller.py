def sum_smaller(nums, target):
    counter = 0
    nums.sort()
    for i in range(len(nums) - 2):
        left = i + 1
        right = len(nums) - 1
        while left < right:
            curr_sum = nums[left] + nums[right] + nums[i]

            if curr_sum < target:
                counter += right - left
                left += 1
            else:
                right -= 1
    return counter


assert sum_smaller([-2, 0, 1, 3], 2) == 2

assert sum_smaller([-2, 0, -1, 3], 2) == 3
