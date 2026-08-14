class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        max_len = float('-inf')
        d = {}
        l = 0

        if not s:
            return 0
        for r in range(len(s)):
            ch = s[r]
            d[ch] = d.get(ch,0)+1
            while d[ch] > 1:
                d[s[l]]-=1
                l += 1
            max_len = max(max_len, r-l+1)

        return max_len

        l = 0
        stack = []
        max_len = 0
        for r in range(len(s)):
            while s[r] in stack:
                stack.pop(0)
                l += 1
            stack.append(s[r])
            max_len = max(max_len, len(stack))
            
        return max_len

        l = 0
        vis = set()
        max_len = 0
        for r in range(len(s)):
            ch = s[r]
            while ch in vis:
                vis.remove(s[l])
                l +=1
            vis.add(ch)
            max_len = max(max_len, (r-l+1))

        return max_len



        vis = set()
        l = 0
        ans = 0
        for r in range(len(s)):
            while s[r] in vis:
                vis.remove(s[l])
                l+=1
            vis.add(s[r])
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