# Time: O(N*logN) | Space: O(N)

class Solution:
    def merge_intervals(self, intervals):
        
        intervals.sort(key = lambda i : i[0]) # sort based on start time of the intervals
        output = [intervals[0]]
        for start, end in intervals[1:]:
            lastEnd = output[-1][1]

            if start <= lastEnd:
                output[-1][1] = max(lastEnd, end)
            else:
                output.append([start, end])

        return output
        
