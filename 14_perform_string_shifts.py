class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        total_shift = 0
        for sh in shift:
            if sh[0] == 0:
                total_shift -= sh[1]
            else:
                total_shift += sh[1]
        print(total_shift)
        if total_shift > 0:
            return Solution.shiftRight(s, total_shift)
        else:
            return Solution.shiftLeft(s, abs(total_shift))
        
    def shiftRight(s, total_shift):
        list_str = list(s)
        for t in range(total_shift):
            tmp = list_str.pop()
            list_str = [tmp] + list_str
        return "".join(list_str)
        
    def shiftLeft(s, total_shift):
        list_str = list(s)
        for t in range(total_shift):
            tmp = list_str[0]
            list_str = list_str[1:] + [tmp]
        return "".join(list_str)
