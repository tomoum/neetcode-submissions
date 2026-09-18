"""

[1, 2, 3, 4] target=6
ans: (2,4) -> [2, 4]

Sol 1:
1. Nested loop check for each value  iterate until the end to find if (target - i) exists 

Time: O(n^2)
Space: O(1)
----------------------------------------

Sol 2: Hashmap (not allowed - space)

1. Check hashmap if target_pair = target - curr_val is available 
2. return the stored index of that key with current index

Time: O(n)
Space: O(n)

----------------------------------------

Sol 3: 2 pointer

- Key: we know if nums[i] >= target ans cannot be in i >=

1. 
"""
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0 
        r = len(numbers) - 1

        while l < r:
            curr_sum = numbers[l] + numbers[r]

            if curr_sum < target:
                l += 1
            elif curr_sum > target:
                r -= 1
            else:
                return [l + 1, r + 1]

        return []

        