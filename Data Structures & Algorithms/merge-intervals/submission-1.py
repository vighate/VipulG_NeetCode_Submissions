class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals = sorted(intervals)
        interval = intervals[0]

        res = []

        intervals = intervals[1:]
        print(intervals)

        for start, end in intervals:

            if end < interval[0]:
                res.append([start, end])
            
            elif interval[1] < start:
                res.append(interval)
                interval = [start,end]

            else:
                interval = [min(start, interval[0]),
                            max(end, interval[1])]

        res.append(interval)

        return res

