class Solution:
    def checkValidString(self, s: str) -> bool:
        low = high = 0
        
        for c in s:
            if c == '(':
                low += 1
            else:
                low -= 1
            
            if c == '(' or c == '*': # c != '')''
                high += 1
            else:
                high -= 1
            
            if high < 0:
                break
            
            low = max(low, 0)
            
        return low == 0
