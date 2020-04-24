class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        x = m^n
        
        x |= x>>1
        x |= x>>2
        x |= x>>4
        x |= x>>8
        x |= x>>16
        
        return m & ~x

    def rangeBitwiseAnd_brute(self, m: int, n: int) -> int:
        
        for num in range(m + 1, n + 1):
            m &= num
        return m
