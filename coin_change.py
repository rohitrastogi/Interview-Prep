#dp
import math
def num_ways_change(num, coins):
    dp = [0]*(num + 1)
    dp[0] = 1
    for i in range(1, num + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] += dp[i - coin]
    return dp[num]


def min_ways_change(num, coins):
    dp = [0]*(num + 1)
    for i in range(1, num + 1):
        comp = math.inf
        for coin in coins:
            if i - coin >= 0:
                comp = min(comp, 1 + dp[i-coin])
            dp[i] = comp
    return dp[num]



coins = [1, 5, 10, 25]
print(min_ways_change(5, coins))


