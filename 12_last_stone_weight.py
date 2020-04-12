class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort()
            first_heaviest_stone = stones[-1]
            second_heaviest_stone = stones[-2]
            
            if first_heaviest_stone == second_heaviest_stone:
                stones.pop()
                stones.pop()
            elif first_heaviest_stone != second_heaviest_stone:
                stones.pop()
                stones[-1] = first_heaviest_stone - second_heaviest_stone
                
        if not stones:
            return 0
        return stones[0]
