class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        if not intervals:
            return []

        intervals = sorted(intervals)

        newInterval = intervals[0]

        res = []

        for start, end in intervals[1:]:
            if end < newInterval[0]:
                res.append([start, end])
            elif newInterval[1] < start:
                res.append(newInterval)
                newInterval = [start, end]
            else:
                newInterval = [min(start, newInterval[0]),
                            max(end, newInterval[1])]
        res.append(newInterval)
        return res
        
        intervals = sorted(intervals)

        res = []

        newInterval = intervals[0]

        for start, end in intervals[1:]:

            if end < newInterval[0]:
                res.append([start, end])

            elif newInterval[1] < start:
                res.append(newInterval)
                newInterval = [start, end]

            else:
                newInterval = [min(start, newInterval[0]), 
                               max(end, newInterval[1])]

        res.append(newInterval)

        return res