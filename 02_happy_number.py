class Solution:
    def isHappy(self, n: int) -> bool:
        
        if n < 0:
            return False
        if n == 1:
            return True
        
        result = n
        values_we_have_seen = set()

        while result != 1:
            sum_digits = Solution.sum_digits(result)
            if sum_digits not in values_we_have_seen:
                values_we_have_seen.add(sum_digits)
            elif sum_digits in values_we_have_seen:
                return False
            if sum_digits == 1:
                return True
            result = sum_digits   
                
    def sum_digits(n):
        sum = 0
        number_components = list(str(n))
        for num in number_components:
            sum += int(num)**2
        return sum
