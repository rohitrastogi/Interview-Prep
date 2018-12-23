#d[row][col] represents the lonogest_comon_subsequence between s1[0:col + 1] and s2[0:row + 1]
def longest_common_subsequence(s1, s2):
    dp = [[0] * (len(s1) + 1) for row in range(len(s2) + 1)]
    for row in range(1, len(dp)):
        for col in range(1, len(dp[0])):
            if (s2[row - 1] != s1[col - 1]):
                dp[row][col] = max(dp[row - 1][col], dp[row][col - 1])
            else:
                dp[row][col] = 1 + dp[row - 1][col - 1]
    return dp[len(s2)][len(s1)]

print(longest_common_subsequence('banana', 'anna'))