# O(N ) time | O(N) space

class Solution(object):
    def depthSum(self, nestedList):

        def depthSumDfsHelper(nested_list, depth):
            total = 0
            for nested in nested_list:
                if nested.isInteger():
                    total += nested.getInteger() * depth
                else:
                    total += depthSumDfsHelper(nested.getList(), depth + 1)
            return total

        return depthSumDfsHelper(nestedList, 1)

        
