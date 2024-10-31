

def minCostClimbingStairs(cost):
    n = len(cost)
    dp = [-1 for _ in range(n)]
    dp[0],dp[1] = cost[0],cost[1]
    for i in range(2, n):
        sum = cost[i] + dp[i - 2]
        if sum <= dp[i - 1]:
            dp[i] = sum
        else:
            if i == n - 1:
                dp[i] = dp[i - 1]
            else:
                dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])
    print(cost)
    print(dp)
    return dp[n - 1]


cost = [10,15,20]
# cost = [1,100,1,1,1,100,1,1,100,1]
print(minCostClimbingStairs(cost))