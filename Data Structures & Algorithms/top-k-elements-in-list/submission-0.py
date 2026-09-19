from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        r = []
        for (k, v) in c.most_common(k):
            r.append(k)
        return r