class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0: return 0
        left = 0
        right = 1
        max_len = 1
        cur_len = 1
        while (right < len(s)):
            if s[right] not in s[left:right]:
                right+=1
                cur_len+=1
                max_len = max(cur_len, max_len)
            else:
                while s[right] in s[left:right]:
                    left+=1
                    cur_len-=1
        return max_len