# first version
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        full_product = 1
        zeroes = []
        for i in range(len(nums)):
            if nums[i] != 0:
                full_product *= nums[i]
            else:
                zeroes.append(i)
        if len(zeroes) > 1: 
            return [0]*len(nums)

        output = []
        if zeroes:
            for i in range(len(nums)):
                if nums[i] == 0:
                    output.append(full_product)
                else:
                    output.append(0)
        else:
            for i in range(len(nums)):
                output.append(full_product//nums[i])
        return output
                    
        

class Solution:
  def productExceptSelf(self, nums: List[int]) -> List[int]:
      full_product = reduce(lambda x, y: x*(y if y else 1), nums, 1)
      zeroes_count = nums.count(0)

      if zeroes_count > 1: 
          return [0]*len(nums)

      output = []
      for i in range(len(nums)):
          if zeroes_count:
              output.append(0 if nums[i] else full_product)
          else:
              output.append(full_product//nums[i])
      return output
                    
