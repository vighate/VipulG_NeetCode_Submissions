class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        res = []
        num_set = set(nums)

        for num in num_set:
            if num-1 not in num_set:
                seq = [num]
                curr = num

                while curr+1 in num_set:
                    seq.append(curr+1)
                    curr += 1

                if len(res) < len(seq):
                    res = seq
        
        return len(res)