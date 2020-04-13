class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        if not nums:
            return 0
        count = 0
        max_length = 0
        cache = {}
        cache[0] = -1
        
        for i, num in enumerate(nums):
            if num == 1:
                count += 1
            else:
                count -= 1
            if count in cache:
                max_length = max(max_length, i - cache[count])
            else:
                cache[count] = i
        
        
        return max_length
    
    def findMaxLength_brute(self, nums: List[int]) -> int:
        num_of_zeros = 0
        num_of_ones = 0
        max_length = 0
        
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if nums[j] == 0:
                    num_of_zeros += 1
                if nums[j] == 1:
                    num_of_ones += 1
                if num_of_zeros == num_of_ones:
                    max_length = max(max_length, num_of_zeros + num_of_ones)
            num_of_zeros = 0
            num_of_ones = 0
                    
        return max_length
