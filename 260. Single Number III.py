class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        n1xn2 = reduce(xor, nums)
        num1 = num2 = 0
        rightmostSetBit = 1
        
        while rightmostSetBit & n1xn2 == 0:
            rightmostSetBit <<= 1
            
        for num in nums:
            if num & rightmostSetBit:
                num1 ^= num
            else:
                num2 ^= num
                
        return [num1, num2]
        
