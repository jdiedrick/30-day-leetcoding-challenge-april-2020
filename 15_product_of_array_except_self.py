class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums) 
        product = 1
        for i in range(0, len(output)):
            output[i] = product
            product *= nums[i]
        
        product = 1
        for i in range(len(output)-1, -1, -1):
            output[i] *= product
            product *= nums[i]

        return output
