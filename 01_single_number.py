class Solution:
    def singleNumber(self, nums: List[int]) -> int:
      
        for num in nums[1:]:
            nums[0] ^= num
            
        return nums[0]
