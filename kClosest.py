# 973. K Closest Points to Origin

# Brute force - simpler: O(N*logN) time | O(N) space

class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        points.sort(key=self.squared_distance)
        return points[:k]

    def squared_distance(self, points):
        return points[0] ** 2 + points[1] ** 2
            
def main():
    points = [[3,3],[5,-1],[-2,4]]
    k = 2
    solution = Solution()
    res = solution.kClosest(points, k)
    print(res)

if __name__ == "__main__": 
    main()
