class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        return Solution.processString(S) == Solution.processString(T)
    
    def processString(string):
        stack = []
        for s in string:
            if s != '#':
                stack.append(s)
            elif stack and s == '#':
                stack.pop()
        return stack
