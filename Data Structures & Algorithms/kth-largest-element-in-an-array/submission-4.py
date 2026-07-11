class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        nums = sorted(nums)

        return nums[len(nums)-k]

        stack = []

        for num in nums:
            stack.append(num)

        while k>1:
            stack.pop()
            k -= 1

        return stack.pop()