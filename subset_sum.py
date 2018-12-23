def solve(target, candidates):
    dp = [[False] * (len(candidates) + 1) for num in range(target + 1)]
    for i in range(len(candidates) + 1):
        dp[0][i] = True

    for row in range(1, target + 1):
        for col in range(1, len(candidates) + 1):
            print(row, col)
            if row < candidates[col - 1]:
                dp[row][col] = dp[row - 1][col-1]
            else:
                dp[row][col] = dp[row - candidates[col-1]][col-1] or dp[row - 1][col-1]

    return dp[target][len(candidates)]

print(solve(5, [1, 2, 3]))