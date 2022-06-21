# 3. Longest Substring Without Repeating Characters

# O(N * 2) time | O(1) space

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        mp = {}

        ans = 0
        i = 0

        for j in range(len(s)):
            char = s[j]
            if char in mp:
                i = max(mp[s[j]], i)

            ans = max(ans, j - i + 1)
            mp[s[j]] = j + 1


        
        return ans
            
def main():
    s = "abcdeafbdgcbb"
    solution = Solution()
    res = solution.lengthOfLongestSubstring(s)
    print(res)

if __name__ == "__main__": 
    main()
