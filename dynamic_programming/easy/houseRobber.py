

def houseRobber(nums,n):
    if n < 0:
        return 0
    
    
    return max(nums[n] + houseRobber(nums, n - 2), houseRobber(nums, n - 1))

arr = [2,7,9,3,1]
print(houseRobber([2,7,9,3,1], len(arr) - 1))