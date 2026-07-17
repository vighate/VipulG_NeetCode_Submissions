class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals = sorted(intervals)
        prev = intervals[0]
        prevend = prev[1]
        count = 0
        for start, end in intervals[1:]:
            if prevend > start:
                count += 1
                prevend = min(prevend, end)
            else:
                prevend = end

        return count