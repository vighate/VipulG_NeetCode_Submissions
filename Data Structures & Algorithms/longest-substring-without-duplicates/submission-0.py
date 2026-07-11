class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
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