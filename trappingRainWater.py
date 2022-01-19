# Brute force O(N^2) time, O(1) space
class Solution(object):
    def trap(self, height):
        if not height: return 0
        
        left, right = 0, len(height) - 1
        res = 0
        for i, val in enumerate(height):
            left = 0 if i == 0 else max(height[:i]) # O(N) time: we're iterating through the array, worst case: O(N)
            right = 0 if i == len(height) - 1 else max(height[i + 1:])
            res += max(0, min(left, right) - val)
        return res
