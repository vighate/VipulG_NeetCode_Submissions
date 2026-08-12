class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        l = 0
        max_freq = 0
        ans = 0
        d = {}

        for r in range(len(s)):
            ch = s[r]
            d[ch] = d.get(ch,0)+1

            max_freq = max(d[ch], max_freq)

            while (r-l+1) - max_freq > k:
                d[s[l]] -= 1
                l +=1
            ans = max(ans, r-l+1)

        return ans