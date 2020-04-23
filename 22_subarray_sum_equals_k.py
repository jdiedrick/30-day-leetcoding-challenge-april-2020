"""
https://www.youtube.com/watch?v=AmlVSNBHzJg
"""

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        running_sum = 0
        arrays_that_equal_k = 0
        sum_freq = { 0: 1} # we have seen a sum of zero once (at the beginning)
        for num in nums:
            running_sum += num
            
            if (running_sum - k) in sum_freq:
                arrays_that_equal_k += sum_freq[running_sum - k]
            if running_sum not in sum_freq:
                sum_freq[running_sum] = 1
            else:
                sum_freq[running_sum] += 1
            
        return arrays_that_equal_k
