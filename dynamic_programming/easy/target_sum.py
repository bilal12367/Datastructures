

def targetSumDp(nums, target):
    n = len(nums)
    dp = [[-1 for _ in range(target + 1)] for _ in range(n + 1)]
    for i in range(n + 1):
        for j in range(target + 1):
            if i == 0:
                dp[i][j] = 0
            if j == 0:
                dp[i][j] = 1
    
    for i in range(1 , n + 1):
        for j in range(1, target + 1):
            if j > 0:
                dp[i][j] = dp[i - 1][j - nums[i - 1]] + dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j + nums[i - 1]] + dp[i - 1][j]
    print(dp)
    return dp[n][target]

print(targetSumDp([1, 1, 1, 1, 1], 3))