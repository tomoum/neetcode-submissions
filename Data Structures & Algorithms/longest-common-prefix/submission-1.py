
"""
1. index i determines which char in every word we are checking
2. iterate over all the words checking this next char we care about is common 
3. if we find a str thats too short we STOP exit early
4. if we get to the end of the list we append that char to the return str

Time: O(n^m) n = num of strs | m = len of longest common prefix
Space: O(1)

[bat, bag, bank]

Sol 2: 
1. hash map to keep track of first word
2. iterate over words which the longest common for each word and break if size of common is 0

Time: O(nxm)
Space: O(a) O(1) a = len of first word in list

"""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0
        first_word = strs[0]

        for i in range(len(first_word)):
            for s in strs[1:]:
                if i > len(s) or s[i] != first_word[i]:
                    return first_word[:i]
        return first_word




