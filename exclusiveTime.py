# O(N) time | O(N) space
class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        stack = []
        func_times = [0] * n
        previous_start_time = 0
        
        for log in logs:
            fid, findicator, ftime = log.split(":")
            fid = int(fid)
            ftime = int(ftime)
            
            if findicator == "start": # if functions starts executing
                if stack:
                    func_times[stack[-1]] += ftime - previous_start_time
                stack.append(fid)
                previous_start_time = ftime
            else:
                func_times[stack.pop()] += ftime - previous_start_time + 1
                previous_start_time = ftime + 1
        return func_times
