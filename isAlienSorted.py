# O(M) time, M => total number of characters in words.
class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        hash_map = {}

        for index, val in enumerate(order):
            hash_map[val] = index

        for i in range(len(words) - 1):
            for j in range(len(words[i])):
                if j >= len(words[i + 1]):
                    return False
                if words[i][j] != words[i + 1][j]:
                    if hash_map[words[i][j]] > hash_map[words[i + 1][j]]:
                        return False
                    break
        return True

def main():
    words = ["hello","leetcode"]
    words = ["word","world","row"]
    order = "worldabcefghijkmnpqstuvxyz"
    solution = Solution()
    res = solution.isAlienSorted(words, order)
    print(res)

if __name__ == "__main__": 
    main()
        
