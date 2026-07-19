from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        need = Counter(t)
        need_len = len(need)
        have = 0
        res = [-1,-1]
        l = 0
        window = {}
        max_len = float('inf')
        for r in range(len(s)):
            ch = s[r]
            window[ch] = window.get(ch,0)+1
            if ch in need and window[ch] == need[ch]:
                have += 1
            while have >= need_len:
                if r-l+1<max_len:
                    max_len = r-l+1
                    res = [l,r]
                left_ch = s[l]
                window[left_ch]-=1
                if left_ch in need and window[left_ch] < need[left_ch]:
                    have -= 1
                l+=1

        l,r = res
        return s[l:r+1]


        
        need = Counter(t)
        need_len = len(need)

        window = {}
        have = 0
        max_len = float('inf')

        left = 0
        res = [-1,-1]

        for right in range(len(s)):
            c = s[right]
            window[c] = window.get(c,0) + 1

            if c in need and window[c] == need[c]:
                have += 1

            while have >= need_len:
                if right-left+1 < max_len:
                    max_len = right-left+1
                    res = [left, right]

                left_ch = s[left]
                window[left_ch] -= 1

                if left_ch in need and window[left_ch] < need[left_ch]:
                    have -= 1
                
                left += 1


        l,r = res
        return s[l:r+1]