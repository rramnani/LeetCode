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

 # O(N) time | O(1) space
 class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height) - 1
        res = 0
        maxLeft, maxRight = height[left], height[right]

        while left < right:
            if maxLeft <= maxRight:
                left += 1
                maxLeft = max(maxLeft, height[left])
                print("maxLeft = ", maxLeft)
                res += maxLeft - height[left]
                print("I'm bounded by left = ", res)
            else:
                right -= 1
                maxRight = max(maxRight, height[right])
                print("maxRight = ", maxRight)
                res += maxRight - height[right]

        return res
