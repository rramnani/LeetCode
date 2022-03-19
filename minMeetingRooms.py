# Optimized - sorting, O(N*logN) time | O(N) space
class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        start = sorted([i[0] for i in intervals])
        end = sorted([i[1] for i in intervals])
        print(start, end)
        count, res = 0, 0
        s,e = 0, 0
        while s <  len(intervals):
            if start[s] < end[e]:
                s += 1
                count += 1
            else:
                count -= 1
                e += 1
            res = max(res, count)
        return res
