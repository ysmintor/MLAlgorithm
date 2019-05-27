from typing import List
# 66. Plus One
# Given a non-empty array of digits representing a non-negative integer, plus one to the integer.
#
# The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.
#
# You may assume the integer does not contain any leading zero, except the number 0 itself.
#
# Example 1:
# Input: [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Example 2:
# Input: [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.
# Runtime: 28 ms, faster than 99.76% of Python3 online submissions for Plus One.
# Memory Usage: 13.1 MB, less than 70.80% of Python3 online submissions for Plus One.
# also learn something from typing package https://docs.python.org/3/library/typing.html


class Solution:
    def plusOne(self, digits: List[int])->List[int]:
        index = len(digits) - 1
        carry = 0
        while index >= 0:
            carry = 1 if digits[index] == 9 else 0
            if carry == 1:
                digits[index] = 0
                index -= 1
            else:
                digits[index] += 1
                break

        if carry == 1:
            digits.insert(0, 1)

        return digits


if __name__ == '__main__':
    solution = Solution()

    print(solution.plusOne([9]))