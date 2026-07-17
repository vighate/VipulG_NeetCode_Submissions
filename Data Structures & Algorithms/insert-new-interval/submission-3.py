class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        res = []

        for start, end in intervals:

            if end < newInterval[0]:
                res.append([start, end])
            elif newInterval[1] < start:
                res.append(newInterval)
                newInterval = [start, end]
            else:
                newInterval = [min(newInterval[0], start),
                                max(newInterval[1], end)]

        res.append(newInterval)
        return res