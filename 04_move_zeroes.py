class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        tortoise, hare = 0, 0
        
        while tortoise < len(nums) - 1 and hare < len(nums) - 1:
            if nums[tortoise] != 0 and nums[hare] != 0:
                tortoise += 1
                hare += 1
            if hare < len(nums) - 1 and nums[tortoise] == 0:
                hare += 1
                while hare < len(nums) - 1 and nums[hare] == 0:
                    hare += 1
                nums[tortoise], nums[hare] = nums[hare], nums[tortoise]
                tortoise += 1
                hare = tortoise
                
        return nums
