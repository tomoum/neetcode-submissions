"""
Edge Cases:
- handle 0 entries

e.g

1. Case 1:
[1, 1 , 2 , 1, 1, 2, 4]
[2, 1 , 4 , 1, 1, 2, 0]

"""
from dataclasses import dataclass


@dataclass
class Item:
    index: int
    val: int

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack :list[Item]= []

        for curr_temp_i, curr_temp in enumerate(temperatures):
            # Temp is less add to stack
            next_item = Item(index=curr_temp_i, val=curr_temp)
            
            if len(stack) == 0 or curr_temp <= stack[-1].val:
                stack.append(next_item)
                continue

            
            # Unwind until 
            while stack and stack[-1].val < curr_temp:
                prev_temp = stack.pop()
                diff_in_days = curr_temp_i - prev_temp.index
                ans[prev_temp.index] = diff_in_days

            stack.append(next_item)
            
        return ans

            



        