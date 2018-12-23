#dp[idx] is the longest increasing subsequence ending at the x+1th char of seq

def longest_increasing_subsequence(seq):
    dp = [0] * len(seq)
    dp[0] = 1
    for i in range(1, len(seq)):
        for j in range(i):
            if seq[i] > seq[j]:
                dp[i] = max(dp[i], 1 + dp[j])
    return max(dp)


test = [1, 3, 2, 7, 3, 4, 5]
print(longest_increasing_subsequence(test))

