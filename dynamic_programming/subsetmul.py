
def isSubsetMul(nums, n , target,mul, subset):
    if target == mul:
        return subset
    
    if n == 0:
        return False
    
    temp = mul * nums[n-1]
    if temp > target:
        return isSubsetMul(nums, n-1 , target,mul, subset)
    
    return isSubsetMul(nums, n-1 , target,mul, subset) or isSubsetMul(nums, n-1, target ,temp, subset + [nums[n-1]])
