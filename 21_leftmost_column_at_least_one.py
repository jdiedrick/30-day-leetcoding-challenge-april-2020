# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, x: int, y: int) -> int:
#    def dimensions(self) -> list[]:
# https://leetcode.com/discuss/interview-question/341247/facebook-leftmost-column-index-of-1
# used hint 2

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        rows = binaryMatrix.dimensions()[0]
        columns = binaryMatrix.dimensions()[1]
        
        # start at top right
        row = 0
        column = columns - 1
        while row < rows and column >= 0:
            if binaryMatrix.get(row, column) == 1:
                column -= 1
            else:
                row += 1
                
        if column != columns - 1:
            return column + 1
        else:
            return -1
