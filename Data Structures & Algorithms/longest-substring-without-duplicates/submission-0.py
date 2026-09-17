"""

Ex 1: 
z x y z a 
  


Sol 1: Brute Force -  set
1. Iterate for each char add to hash set until duplictate detected 
2. once duplicate in set set that size of the set as the current max_length
3. reset the set and repeat for next index

Time: O(n2) n = num chars in s
Space: O(n) 
----------------------------------------
Sol 2: 
1. left , right iterators
2. Check if char in seen hash map 
    - IF seen - 
        a) max (curr_len=len of dict , global_max_len)
        b) find the index of that duplicate then remove it and everything before it in the dict
        c) reset curr_len
    - ELSE
        a) store char with index in map

Time: O(n)
Space: O(k) k=max length of unique chars

"""

from collections import OrderedDict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        window = OrderedDict()

        for i, char in enumerate(s):
            if char in window:
                max_len = max(len(window), max_len)
                index_of_dupe = window[char]
                while window and index_of_dupe != 0:
                    window.popitem(last=False)
                    index_of_dupe -= 1
                
            window[char] = i
        return max(max_len, len(window))



        