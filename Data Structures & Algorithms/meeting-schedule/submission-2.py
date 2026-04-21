"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        for i in range(len(intervals)):
            x=intervals[i].start
            y=intervals[i].end
            for j in range(i+1,len(intervals)):
                x1=intervals[j].start
                y1=intervals[j].end
                if min(y1,y)>max(x1,x):
                    return False
        return True
