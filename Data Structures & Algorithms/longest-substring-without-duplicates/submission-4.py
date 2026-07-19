class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l = 0
        ans = 0
        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l+=1
            seen.add(s[r])
            ans = max(ans, r-l+1)
        return ans

        
        long_seq = []
        seq = []

        for c in s:
            if c in seq:

                if len(long_seq) < len(seq):
                    long_seq = seq[:]

                while seq[0] != c:
                    seq.pop(0)
                seq.pop(0)

            seq.append(c)

        if len(long_seq) < len(seq):
            long_seq = seq[:]

        return len(long_seq)