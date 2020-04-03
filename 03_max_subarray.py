class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        
        current_prefix_sum = 0
        
        for n in nums:
            current_prefix_sum += n
            if current_prefix_sum > max_sum:
                max_sum = current_prefix_sum
                
            if current_prefix_sum < 0:
                current_prefix_sum = 0
        
        return max_sum
