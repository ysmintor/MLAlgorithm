# LeetCode
# 70. Climbing Stairs
class Solution:
    memo = []

    def climbStairs(self, n: int) -> int:
        self.memo = [0] * n
        print(self.memo)
        return self.climbStep(0, n)

    def climbStep(self, cur: int, step: int) -> int:
        if cur > step:
            return 0
        elif cur == step:
            return 1  # after step one or two at a time to reach final step
        else:
            print('cur', cur)
            if self.memo[cur] > 0:
                return self.memo[cur]

            self.memo[cur] = self.climbStep(cur + 1, step) + self.climbStep(cur + 2, step)
            return self.memo[cur]


if __name__ == '__main__':
    solution = Solution()
    solution.climbStairs(2)