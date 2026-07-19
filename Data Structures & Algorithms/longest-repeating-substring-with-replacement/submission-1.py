class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        l = 0
        max_freq = 0
        window = {}
        ans = 0
        for r in range(len(s)):
            ch = s[r]
            window[ch] = window.get(ch,0)+1
            max_freq = max(max_freq, window[ch])
            while (r-l+1) - max_freq > k:
                window[s[l]]-=1
                l+=1
            ans = max(ans, (r-l+1))
        return ans
