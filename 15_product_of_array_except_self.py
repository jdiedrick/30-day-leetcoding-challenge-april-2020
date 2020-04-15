class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums) 
        
        product = 1
        
        for i in range(0, len(output)):
            output[i] = product
            product *= nums[i]
        print(output)
        product = 1
        
        for i in range(len(output)-1, -1, -1):
            output[i] *= product
            product *= nums[i]

        return output
    
    def productExceptSelf_brute(self, nums: List[int]) -> List[int]: 
        output = []
        if len(nums) == 1:
            return result
  
        for i in range(len(nums)):
            product = 1
            for j in range(len(nums)):
                if j == i:
                    continue
                product *= nums[j]
            output.append(product)
  
        return output
