
class Solution:
    def canPartition(self, nums):
        sum1 = sum(nums)
        if sum1 % 2 == 0:
            sum1 /= 2
            return self.canPartitionDp(nums, len(nums), int(sum1))
        else:
            return False
    
    def canPartitionRec(self, nums, n, target):
        if target == 0:
            return True
        if n == 0:
            return False

        if nums[n - 1] <= target:
            return self.canPartitionRec(nums, n - 1, target - nums[n - 1]) or self.canPartitionRec(nums, n - 1, target)
        else:
            return self.canPartitionRec(nums, n - 1, target)

    def canPartitionDp(self, nums, n , target):

        dp = [[-1 for _ in range(target + 1)] for _ in range(n + 1)]
        for i in range(n + 1):
            for j in range(target + 1):
                if i == 0:
                    dp[i][j] = False
                if j == 0:
                    dp[i][j] = True
        for i in range(1, n + 1):
            for j in range(1, target + 1):
                if nums[i - 1] <= j:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[n][target]


x = Solution()
print(x.canPartition([1,5,11,5]))