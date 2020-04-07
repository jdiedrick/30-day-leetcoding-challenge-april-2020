class Solution:
    def countElements(self, arr: List[int]) -> int:
        cache = {}
        count = 0
        for num in arr:
            if num not in cache:
                cache[num] = num + 1
            if cache[num] in arr:
                count += 1
        return count
