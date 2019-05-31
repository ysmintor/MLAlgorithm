# 3. Longest Substring Without Repeating Characters
# Given a string, find the length of the longest substring without repeating characters.


# Brute force way
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        for i in range(len(s)):
            for j in range(i+1, len(s) + 1):
                if self.allUnique(s[i:j]):
                    max_len = max(max_len, j - i)
        return max_len

    def allUnique(self, sub_str: str) -> bool:
        # check substring is all unique
        return  len(sub_str) == len(set(sub_str))


if __name__ == '__main__':
    solution = Solution()
    print("Test1=", solution.lengthOfLongestSubstring("abcabcbb") == 3)
    print("Test2=", solution.lengthOfLongestSubstring("bbbbb") == 1)
    print("Test3=", solution.lengthOfLongestSubstring("pwwkew") == 3)

