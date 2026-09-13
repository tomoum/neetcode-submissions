class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pair_for_curr = {}
        # target = 5
        for i, curr in enumerate(nums): # curr = 4
            target_pair = target - curr
            if curr in pair_for_curr:
                return [pair_for_curr[curr], i]
            pair_for_curr[target_pair] = i

        return []