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

        intervals = sorted(intervals, key= lambda x: x.start)

        prev = intervals[0]

        flag = True

        for interval in intervals[1:]:

            if prev.end > interval.start:
                flag = False
                prev.end = max(prev.end, interval.end)

            else:
                prev.end = interval.end

        return flag