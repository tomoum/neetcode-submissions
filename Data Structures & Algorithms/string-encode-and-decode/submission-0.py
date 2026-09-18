class Solution:

    SEP = chr(257)

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 1 and strs[0] == "":
            return ""
        return self.SEP.join(strs)


    def decode(self, s: str) -> List[str]:
        if not s:
            return [""]
        strs = []
        prev = 0
        i = 0
        while i < len(s):
            # a S a a a
            if s[i] == self.SEP:
                strs.append(s[prev:i])
                prev = i + 1
            i += 1
        if prev < i:
            strs.append(s[prev:i]) 
        return strs


