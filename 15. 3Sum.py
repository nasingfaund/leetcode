class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        d = {n: i for i, n in enumerate(nums)}
        res = set()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                x, y =  nums[i], nums[j]
                z = x + y
                if d.get(-z, 0) > j:
                    elem = tuple(sorted((x, y, -z)))
                    if elem not in res:
                        res.add(elem)
        return res

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        # [-4, -1, -1, 0, 1, 2]
        result = []
        for i in range(len(nums)):
            if i == 0 and nums[i] == nums[i - 1]: continue
            lo = i + 1
            hi = len(nums) - 1
            target = -nums[i]
            while lo < hi:
                if nums[lo] + nums[hi] == target:
                    result.append([nums[i], nums[lo], nums[hi]])
                    while lo < hi and nums[lo] == nums[lo + 1]: lo += 1
                    while lo < hi and nums[hi] == nums[hi - 1]: hi -= 1
                    lo += 1
                    hi -= 1
                elif nums[lo] + nums[hi] < target:
                    lo += 1
                else:
                    hi -= 1

        return result


class Solution:
    def threeSum(self, nums):
        if not nums:
            return nums
        nums.sort()

        first = 0
        result = []
        while first < len(nums):
            if nums[first] > 0:
                break
            second = first + 1
            third = len(nums) - 1
            while second < third:
                sum3 = nums[first] + nums[second] + nums[third]

                if sum3 == 0:
                    result.append([nums[first], nums[second], nums[third]])
                    while second + 1 < len(nums) and nums[second + 1] == nums[second]:
                        second += 1
                    second +=1
                    third -=1
                    
                elif sum3 < 0:
                    second +=1
                else:
                    third -= 1

            while first + 1 < len(nums) and nums[first + 1] == nums[first]:
                first += 1
            first += 1

        return result



