from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        n = len(s1)
        m = len(s2)

        counter = Counter(s1[:])
        print(counter)

        window_count = Counter(s2[:n])
        print(window_count)

        if window_count == counter:
            return True

        for i in range(n,m):
            window_count[s2[i]] += 1

            window_count[s2[i-n]] -= 1

            if window_count[s2[i-n]] == 0:
                del window_count[s2[i-n]]
            
            if window_count == counter:
                return True

        return False        
        