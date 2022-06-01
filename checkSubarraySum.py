class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Brute force O(N^2) time | O(1) space
        # current_sum = 0
        # for i in range(len(nums)):
        #     for j in range(i, len(nums)):
        #         current_sum += nums[j]
        #         if j - i + 1 >= 2 and current_sum % k == 0:
        #             return True
        #     current_sum = 0

        # Dictionary: O(N) time | O(min(N, k) space
        dict = {0 : -1}
        current_sum = 0

        for i, n in enumerate(nums):
            current_sum += n
            if k != 0:
                current_sum = current_sum % k

            if current_sum not in dict:
                dict[current_sum] = i
            elif i - dict[current_sum] >= 2:
                return True

        return False
        




def main():
    #A = [[1,2],[1,3],[2,3]]
    nums = [23,2,6,4,7]
    k = 13
    solution = Solution()
    res = solution.checkSubarraySum(nums, k)
    print(res)

if __name__ == "__main__": 
    main()
