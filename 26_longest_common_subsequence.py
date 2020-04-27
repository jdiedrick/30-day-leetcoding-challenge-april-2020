"""
help from: https://www.youtube.com/watch?v=Qf5R-uYQRPk
"""

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = {}
        
        def LCSHelper(text1, text2, m, n):
            if (m, n) in dp:
                return dp[(m, n)]
            result = 0
            if m == 0 or n == 0:
                return result
            if text1[m-1] == text2[n-1]:
                result =  1 + LCSHelper(text1, text2, m - 1, n - 1)
            else:
                result = max(LCSHelper(text1, text2, m - 1, n), LCSHelper(text1, text2, m, n - 1))
            dp[(m, n)] = result
            return result
    
        return LCSHelper(text1, text2, len(text1), len(text2))
