from collections import deque
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0: return 0
        max_len = 1
        left = 0
        substring = set()
        for char in s:
            if char not in substring:
                substring.add(char)
                max_len = max(len(substring), max_len)
            else:
                while char in substring:
                    substring.remove(s[left])
                    left += 1
                substring.add(char)
        return max_len