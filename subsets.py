# 78. Subsets


# O(N * 2^N) time | O(N) space

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        subset = []
        def dfs(i):
            if i >= len(nums):
                result.append(subset.copy())
                return
            
            subset.append(nums[i])
            dfs(i + 1)
            
            subset.pop()
            dfs(i + 1)
        dfs(0)
        return result
            
def main():
    nums = [1,2,3]
    solution = Solution()
    res = solution.subsets(nums)
    print(res)

if __name__ == "__main__": 
    main()
