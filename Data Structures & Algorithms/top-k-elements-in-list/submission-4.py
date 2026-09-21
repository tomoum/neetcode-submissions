from collections import defaultdict, Counter
"""
Sol 
1. Count for each num in array -> dict [num, freq]
2. Buckets for frequencies: list of lists where the index in outer list is the frequency
3. iterate backwards and append to result until k elements found

[1] [ 4, 7 , 8]
[2] [ 4]
"""
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)

        ans = []
        freq = [[] for i in range(len(nums) + 1)]

        for num, count in count.items():
            freq[count].append(num)
        
        for rank in reversed(freq):
            for num in rank:
                ans.append(num)
                if len(ans) == k:
                    return ans
        return ans


        


        