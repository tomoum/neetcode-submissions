"""

[ 2, 15, 77] kg

1. [15 77] -> [ 2 62]
2. return 60

Return : last remain weight OR 0

Sol 1: 
1. Create a max heap of stones
2. pop 2 then check weights 
    - EQ : nothing to do loop again 
    - |diff| : push back in the heap 
3. loop until len stones heap <= 1

"""
import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Create Max heap
        stone_heap = []
        for stone in stones:
            heapq.heappush(stone_heap, -stone)
        
        while len(stone_heap) >= 2:
            x, y = -heapq.heappop(stone_heap), -heapq.heappop(stone_heap)

            if x == y:
                continue
            diff = abs(x - y)
            heapq.heappush(stone_heap, -diff)

        return -stone_heap.pop() if stone_heap else 0








