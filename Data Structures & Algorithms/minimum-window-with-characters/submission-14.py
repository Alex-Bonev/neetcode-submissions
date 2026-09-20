from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if (len(s) <= 1 and s != t): return ""
        # if s == t: return s

        seen = {i: 0 for i in t}

        left = 0
        right = 0
        t = Counter(t)

        compare = Counter(s)

        if (any(compare[k] < t[k] for k in t)):
            return ""

        shortest_idx = [0, 0]

        #first step is to find ANY valid window
        while(any(seen[k] < t[k] for k in seen) and right < len(s)):
            if s[right] in t:
                seen[s[right]]+=1
            right += 1
        # now, we need to cut any fluff from the left side
        while(True):
            #we are checking if removing it takes us below threshold
            if s[left] in t:
                if seen[s[left]]-1 < t[s[left]]:
                    #if so, we do not shift left and stop
                    break
                else:
                    seen[s[left]]-=1
            # otherwise, left points to a random or repeat value
            left += 1
        
        #at this point, we have THE FIRST minimum window.
        # This window will never get larger, so we now shift left and right together, but we will also mark this.
        shortest_idx = [left, right]
        
        while (right < len(s)):

            if s[left] in t:
                seen[s[left]] -= 1
            
            left  += 1
            right += 1
            

            if s[right-1] in t:
                seen[s[right-1]] += 1
                while(all(seen[k] >= t[k] for k in seen)):
                    if s[left] in t:
                        if seen[s[left]]-1 < t[s[left]]:
                            break
                        seen[s[left]] -= 1
                    left += 1
            
            if right - left < shortest_idx[1] - shortest_idx[0]:
                shortest_idx = [left, right]

        return s[shortest_idx[0]:shortest_idx[1]]



        





