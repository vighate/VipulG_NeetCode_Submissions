class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        res = []

        for start, end in intervals:

            if end < newInterval[0]:
                res.append([start, end])

            elif newInterval[1] < start:
                res.append([newInterval[0], newInterval[1]])
                newInterval = [start, end]

            else:
                newInterval = [min(start, newInterval[0]),
                                max(end, newInterval[1])]

        res.append(newInterval)

        
        return res