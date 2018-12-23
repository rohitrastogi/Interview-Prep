def numDistinct(s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        len_s, len_t = len(s), len(t)
        dp = [[0] * (len_s + 1) for _ in range(len_t + 1)]

        for j in range(1, len_s + 1):
            dp[0][j] = 1
        for i in range(1, len_t + 1):
            dp[i][0] = 0

        dp[0][0] = 1

        for i in range(1, len_t + 1):
            for j in range(1, len_s + 1):
                if s[j-1] == t[i-1]:
                    dp[i][j] = dp[i-1][j-1] + dp[i][j-1]
                else:
                    dp[i][j] = dp[i][j-1]
        print(dp)

        return dp[len_t][len_s]

print(numDistinct('rabbbb', 'rab'))