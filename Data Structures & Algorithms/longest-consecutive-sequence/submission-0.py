class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        num_set = set(nums)
        print(num_set)

        long_seq = []

        for num in num_set:
            if num-1 not in num_set:
                seq = [num]
                curr = num

                while curr+1 in num_set:
                    seq.append(curr+1)
                    curr += 1

                if len(seq) > len(long_seq):
                    long_seq = seq
        return len(long_seq)
        
        # # sorting 1
        # print(sorted(nums))

        # # sorting 2
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] > nums[j]:
        #             nums[i], nums[j] = nums[j], nums[i]

        # print(nums)

        # # sorting 3

        # res = [nums[0]]

        # for i in range(1, len(nums)):

        #     curr = nums[i]
        #     j = len(res)-1

        #     while j>=0 and res[j] > curr:
        #         j-=1
            
        #     res.insert(j+1, curr)
        
        # print(res)

