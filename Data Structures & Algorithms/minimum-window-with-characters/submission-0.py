from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if len(s) < len(t):
            return ""

        need = Counter(t)
        print(need)
        need_len = len(need)
        have = 0

        window = {}

        res_len = float('inf')

        left = 0
        res = [-1,-1]

        for right in range(len(s)):
            c = s[right]

            window[c] = window.get(c,0) + 1

            if c in need and window[c] == need[c]:
                have += 1

            while have == need_len:
                if right-left+1 < res_len:
                    res_len = right-left+1
                    res = [left, right]
                
                left_char = s[left]
                window[left_char] -= 1

                if left_char in need and window[left_char] < need[left_char]:
                    have -= 1
                left += 1

        l, r = res
        return s[l:r+1]

            











