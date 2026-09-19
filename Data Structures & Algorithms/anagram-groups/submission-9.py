from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        connect = defaultdict(list)
        for s in strs:
            chars = [0] * 26
            for char in s:
                chars[ord(char)-97] += 1
            fst = tuple(chars)
            connect[fst].append(s)
        return list(connect.values())