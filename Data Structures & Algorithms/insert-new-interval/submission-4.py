class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        if not newInterval:
            return intervals

        res = []

        for start, end in intervals:

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






        res = []

        for start, end in intervals:

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
