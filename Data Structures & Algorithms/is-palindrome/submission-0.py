"""
Req:
1. ignore non alphanumeric
2. 

Edge cases:
1. len 1 - OK
2. len 2 - OK
3. len even 
4. len odd
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [char.lower() for char in s if char.isalnum()]
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return j <= i