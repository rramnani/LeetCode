# O(N) time | O(N) space
class Solution(object):
    def largestRectangleArea(self, heights):
        stack = []
        maxArea = 0
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index
            stack.append((start, h))

        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        return maxArea


def main():
    #A = [[1,2],[1,3],[2,3]]
    heights = [2,1,5,6,2,3]
    solution = Solution()
    res = solution.largestRectangleArea(heights)
    print(res)

if __name__ == "__main__": 
    main()
