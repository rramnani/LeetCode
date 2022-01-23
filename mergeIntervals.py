# O(N* logN) time | O(N) space
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key = lambda i: i[0])
        output = [intervals[0]] # initialize to the first interval
        print(intervals, output)
        for start, end in intervals[1:]:
            lastEnd = output[-1][1]
            
            if start <= lastEnd:
                output[-1][1] = max(lastEnd, end)
            else:
                output.append([start,end])
        return output
