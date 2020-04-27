class Solution:
    def canJump(self, nums: [int]) -> bool:
        life = 1
        for num in nums[:-1]:
            life = max(life - 1, num)

            if life == 0:
                return False

        return True

