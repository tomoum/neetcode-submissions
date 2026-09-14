class Solution:
    def isValid(self, s: str) -> bool:
        pairs = { 
            ')': '(',
            '}': '{',
            ']': '[',
        }

        stack = []

        for char in s:
            # close
            if char in pairs:
                exp = pairs[char]
                if not stack or stack.pop() != exp:
                    return False
            else:
                stack.append(char)
        
        return len(stack) == 0

