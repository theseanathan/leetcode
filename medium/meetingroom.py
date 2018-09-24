# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if len(intervals) <= 1:
            return len(intervals)
        
        min_num = 0 
        
        for i in range(len(intervals)):
            add_min = True
            if add_min and not on_top:
                print('Incrementing Min')
                min_num += 1        
            
        return min_num
