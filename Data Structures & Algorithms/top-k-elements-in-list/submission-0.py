from collections import Counter
"""
Problem:
1. count top k freq nums

Brute Force:
1. iterte on elements [O(n)]
    - keep hashmap with count of each element
2. Find max k in all pairs [O(n log n)]

Complexity: 
Time: O(n log n) 
Space: O(n) - Hashmap

Better

1. Count number of all element
2. Maintan Min heap of k elements


"""

import heapq
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        totals = defaultdict(int)
        for num in  nums:
            totals[num] += 1
        return heapq.nlargest(k, totals)



