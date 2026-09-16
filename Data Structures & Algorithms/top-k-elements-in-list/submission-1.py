from collections import Counter
"""
Problem:
1. count top k freq nums
----------------------------------------
Brute Force:
1. iterte on elements [O(n)]
    - keep hashmap with count of each element
2. Sort to find max k in all pairs [O(n log n)]

Complexity: 
Time: O(n log n) 
Space: O(n) - Hashmap
----------------------------------------
Better - Min Heap

1. Count number of all element
2. Maintan Min heap of k elements

Complexity: 
Time: O(n log k)
Space: O(n)
----------------------------------------
Better - Buckets

1. Count the num and place it directly in a pre allocated list by index - where the index represent the current count of that num
2. return the last k non-empty indexes

Complexity:
Time: O(n)
Space : O(n)
"""

import heapq
from collections import defaultdict, Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        totals = defaultdict(int)
        for num in  nums:
            totals[num] += 1
        
        return [val for key, val in heapq.nlargest(k, totals.items(), key= lambda x: x[1])]



