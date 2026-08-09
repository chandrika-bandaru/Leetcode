class Solution:

    def stoneGameII(self, piles: list[int]) -> int:
        n = len(piles)
        suffix_sum = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + piles[i]

        memo = {}

        def dp(i, m):
            if i + 2 * m >= n:
                return suffix_sum[i]
            if (i, m) in memo:
                return memo[(i, m)]

            min_opponent_stones = float("inf")
            for x in range(1, 2 * m + 1):
                min_opponent_stones = min(
                    min_opponent_stones, dp(i + x, max(m, x))
                )

            memo[(i, m)] = suffix_sum[i] - min_opponent_stones
            return memo[(i, m)]

        return dp(0, 1)