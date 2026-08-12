class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        l = 0
        d = {}
        max_freq = 0
        max_len = 0
        for r in range(len(s)):
            ch = s[r]
            d[ch] = d.get(ch,0) + 1
            max_freq = max(max_freq, d[ch])
            while (r-l+1) - max_freq > k:
                d[s[l]]-=1
                l +=1
            
            max_len = max(max_len, r-l+1)
        
        return max_len