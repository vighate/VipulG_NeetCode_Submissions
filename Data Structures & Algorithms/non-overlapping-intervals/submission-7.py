class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals = sorted(intervals)

        prev = intervals[0]
        prevend = prev[1]
        count = 0
        for start, end in intervals[1:]:
            if prevend > start:
                count += 1
                if prevend > end:
                    prevend = min(prevend, end)
            else:
                prevend = end
        return count




        intervals = sorted(intervals)

        prev = intervals[0]

        count = 0 

        for start, end in intervals[1:]:
            if start < prev[1]:
                count += 1
                if end < prev[1]:
                    prev = [start, end]
            else:
                prev = [start, end]

        return count