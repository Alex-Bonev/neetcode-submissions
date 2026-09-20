from collections import deque
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        left = 0
        substring = set()
        for char in s:
            while char in substring:
                substring.remove(s[left])
                left += 1
            substring.add(char)
            max_len = max(len(substring), max_len)
        return max_len