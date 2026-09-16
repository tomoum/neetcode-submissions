"""

Problem:
- Find Max Profit
- Can only sell later not before

Ex 1
[10, 1, 5, 6, 7, 1]
Ans: 6 - buy 1 sell 7

[5, 4, 6, 1, 1]


Sol 1: Brute Force
1. For every day iterate to the end to find max possible profit
2. Ans: Keep max value and update after calc at each index

Time: O(n2)
Space: O(1) - only current max_profit
----------------------------------------
Sol 2: 2 pointer 
1. Left -> move when less price found
2. Right -> move when Higher price found
3. Ans: right - left (values)

Time: O(n)
Space: O(1)
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, len(prices) - 1
        buy, sell = left, right

        while left < right:
            if prices[left] < prices[buy]:
                buy = left
            if prices[right] > prices[sell]:
                sell = right
            left += 1
            right -= 1
            

        
        return max(prices[sell] - prices[buy], 0)