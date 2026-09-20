class Solution:

    def encode(self, strs: List[str]) -> str:
        result = []
        for s in strs:
            result.append(str(len(s))+"#")
            result.append(s)
        return "".join(result)

    def decode(self, s: str) -> List[str]:
        length = 0
        i = 0
        result = []
        while i < len(s)-1:
            if (length == 0 and s[i] == "0"):
                i += 2
                result.append("")
            elif (s[i] == "#"):
                result.append(s[i+1:i+1+length])
                i = i+1+length
                length = 0
            else:
                length *= 10
                length += int(s[i])
                i += 1
            
        return result
