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

        intervals = sorted(intervals, key= lambda x:x.start)

        prev = intervals[0]
        prevEnd = prev.end

        flag = True

        for interval in intervals[1:]:

            if prevEnd > interval.start:
                flag = False
                prevEnd = min(prevEnd, interval.end)
            else:
                prevEnd = interval.end

        return flag