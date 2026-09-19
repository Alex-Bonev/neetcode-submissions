from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
        connect = defaultdict(list)
        key = 1
        for s in strs:
            for char in s:
                key *= primes[ord(char)-97]
            connect[key].append(s)
            key = 1
        return list(connect.values())