class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        stack = []
        max_area = 0
        nums = heights
        
        for i,h in enumerate(nums):

            start = i

            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                max_area = max(max_area, height*(abs(i-index)))
                start = index

            stack.append((start,h))
        
        for i, h in stack:
            max_area = max(max_area, h*(len(nums)-i))


        return max_area

        max_area = 0

        stack = []

        for i, h in enumerate(heights):
            start = i

            while stack and stack[-1][1] > h:
                index, height = stack.pop()

                max_area = max(height*(i-index), max_area)

                start = index
            
            stack.append((start, h))

        for i, h in stack:
            max_area = max(max_area , h*(len(heights)-i))

        return max_area