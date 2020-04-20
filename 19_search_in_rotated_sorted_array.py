class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        
        # find the disjoint index
        disjoint_index = Solution.findDisjointIndex(nums) # O(log n)
                
        # check to see if target is in the left half or right half
        if disjoint_index == 0: # binary search entire array
            return Solution.binarySearch(nums, 0, len(nums) - 1, target) # O (log n)
        elif nums[0] <= target and nums[disjoint_index - 1] >= target: # binary search left
            return Solution.binarySearch(nums, 0, disjoint_index, target) # O(log n)
        else: #binary search right
            return Solution.binarySearch(nums, disjoint_index, len(nums) - 1, target) # O(log n)
        
    def findDisjointIndex(nums):
        element_to_compare = nums[-1]
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            curr_val = nums[mid]
            if element_to_compare < curr_val:
                left = mid + 1
            elif element_to_compare >= curr_val:
                right = mid - 1
        return left

    def binarySearch(nums, left, right, target):
        
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
