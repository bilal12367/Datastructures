
def isSubsetSum(nums, n, target):
    if target == 0:
        return True
    
    if n == 0:
        return False
    
    if nums[n-1] > target:
        return isSubsetSum(nums, n-1, target)

    return isSubsetSum(nums, n-1, target) or isSubsetSum(nums, n-1, target - nums[n-1])

def subsetSumDP(nums, n , target):
    t = [[False for i in range(target+1)] for j in range(n+1)]
    for i in range(n + 1):
        t[i][0] = True

    for i in range(1,n+1):
        for j in range(1,target+1):
            if j == 0:
                t[i][j] = True
            if i == 0:
                t[i][j] = False
                
            if nums[i-1] > j:
                t[i][j] = t[i-1][j]
            else: 
                t[i][j] = t[i-1][j] or t[i - 1][j - nums[i-1]]
    return t[n][target]

# def subsetSumDP1(nums, target):
#     n = len(nums)

#     # Create a table to store results of subproblems
#     dp = [[False] * (target + 1) for _ in range(n + 1)]

#     # Base case: an empty subset can achieve a sum of 0
#     for i in range(n + 1):
#         dp[i][0] = True

#     # Fill the table using the top-down approach
#     for i in range(1, n + 1):
#         for j in range(1, target + 1):
#             if nums[i - 1] <= j:
#                 # Include the current element or exclude it
#                 dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]
#             else:
#                 # If the current element's value is greater than the current sum, exclude it
#                 dp[i][j] = dp[i - 1][j]

#     # The result is stored in the bottom-right cell of the table
#     return dp[n][target]

def subsetSumDP2(arr, target):
    n = len(arr)
    t = [[False for i in range(target+1)] for j in range(n+1)]

    for i in range(n+1):
        t[i][0] = True
    
    for i in range(1,n+1):
        for j in range(target+1):
            
            if j == 0:
                t[i][j] = True
        
            if i == 0:
                t[i][j] = False
            
            if arr[i - 1] > j:
                t[i][j] = t[i-1][j]
            else:
                t[i][j] = t[i-1][j] or t[i-1][j - arr[i - 1]]

    return t[n][target]

if __name__ == '__main__':
    arr = [6, 3, 5, 2, 4]
    target = 19
    print(subsetSumDP2(arr,target))