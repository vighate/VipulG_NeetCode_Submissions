from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False
        s1_count = Counter(s1)
        n = len(s1)
        m = len(s2)
        window = Counter(s2[:n])
        if window == s1_count:
            return True
        for i in range(n,m):
            ch = s2[i]
            window[ch]+=1
            window[s2[i-n]]-=1
            if window[s2[i-n]]==0:
                del window[s2[i-n]]
            if window == s1_count:
                return True
        return False

        
        if len(s1) > len(s2):
            return False

        n = len(s1)
        m = len(s2)

        s1_counter = Counter(s1)

        window_count = Counter(s2[:n])

        if window_count == s1_counter:
            return True

        for i in range(n,m):
            c = s2[i]
            window_count[c] += 1
            window_count[s2[i-n]] -= 1

            if window_count[s2[i-n]] == 0:
                del window_count[s2[i-n]]

            if window_count == s1_counter:
                return True

        return False
        