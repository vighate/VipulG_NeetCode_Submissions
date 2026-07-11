"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        if not intervals:
            return True

        intervals.sort(key=lambda x: x.start)
        
        print(intervals[0].end)

        prevEnd = intervals[0].end

        flag = True

        for interval in intervals[1:]:

            if prevEnd > interval.start:
                flag = False
            else:
                prevEnd = interval.end
        
        return flag
