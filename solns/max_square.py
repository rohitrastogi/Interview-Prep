# calculate maximal square in a matrix of 1s and 0s
# dynamic programming 
# strategy: dp[r, c] = size of the max square with where (r, c) is the bottom right point of the square

def maximal_square(matrix):
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    dp = [[0 for c in range(num_cols)] for r in range(num_rows)]
    for r in range(num_rows):
        dp[r][0] = matrix[r][0]
    for c in range(num_cols):
        dp[0][c] = matrix[0][c]
    for r in range(1, num_rows):
        for c in range(1, num_cols):
            if matrix[r][c] == 1:
                dp[r][c] = min(dp[r-1][c], dp[r-1][c-1], dp[r][c-1]) + 1
            else:
                dp[r][c] = 0 
    return max([max(row) for row in dp])

test = [
    [0, 1, 1, 0, 1],
    [1, 1, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0]
]

print(maximal_square(test))
    