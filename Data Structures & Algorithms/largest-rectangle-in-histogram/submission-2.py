class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        
        nums = heights
        stack = []
        max_val = 0

        for i, h in enumerate(nums):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                max_val = max(max_val, height*(abs(i-index)))
                start = index

            stack.append((start,h))

        for i, h in stack:
            max_val = max(max_val, h*(len(nums)-i))

        return max_val