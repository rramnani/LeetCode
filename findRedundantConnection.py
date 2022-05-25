# Union Find O(N) time | O(N) space            

class Solution:
    def findRedundantConnection(self, edges):
        parent = [i for i in range(len(edges) + 1)]
        rank = [1] * (len(edges) + 1)

        def find(n):
            p = parent[n]

            while p != parent[p]:
                p = parent[parent[p]]
                p = parent[p]

            return p
        def union(n1, n2):

            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return False
            if rank[p1] >= rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]

            return True
        for u1, u2 in edges:
            if not union(u1, u2):
                return [u1, u2]


def main():
    #A = [[1,2],[1,3],[2,3]]
    A = [[1,2],[2,3],[3,4],[1,4],[1,5]]
    solution = Solution()
    res = solution.findRedundantConnection(A)
    print(res)

if __name__ == "__main__": 
    main()
