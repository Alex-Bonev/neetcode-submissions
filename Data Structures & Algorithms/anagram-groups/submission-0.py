class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        connect = {}
        for i, s in enumerate(strs):
            srt = "".join(sorted(s))
            if (srt not in connect):
                connect[srt] = len(result)
                result.append([s])
            else:
                result[connect[srt]].append(s)
        return result