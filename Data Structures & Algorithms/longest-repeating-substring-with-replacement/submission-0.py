class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        left = 0
        window = {}
        max_ch = 0
        ans = 0
        for right in range(len(s)):
            ch = s[right]

            window[ch] = window.get(ch,0)+1

            max_ch = max(max_ch, window[ch])

            if (right-left+1) - (max_ch) > k:
                window[s[left]]-= 1
                left +=1

            ans = max(ans, right-left+1)

        return ans


