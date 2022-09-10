# count sort
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red, white, blue = 0, 0, 0
        
        for num in nums:
            if num == 0:
                red += 1
            elif num == 1:
                white +=1
            elif num == 2:
                blue += 1
        i = 0
        while red or white or blue:
            if red:
                nums[i] = 0
                red -=1
            elif white:
                nums[i] = 1
                white -=1
            elif blue:
                nums[i] = 2
                blue -=1
            i+=1
            
                
        return nums

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        right = len(nums) - 1
        i = 0 
        while i <= right:
            if nums[i] == 0:
                nums[i], nums[left] = nums[left], nums[i]
                left +=1
                i += 1
            elif nums[i] == 1:
                i += 1
            elif nums[i] == 2:
                nums[i], nums[right] = nums[right], nums[i]
                right -= 1
                
        return nums
