import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = nums
        self.k = k
        heapq.heapify(self.heap)

    def balance(self)->None:
        # Keep only k largest discard smallest values until then
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)
        

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        self.balance()
        return self.heap[0]
        

        
