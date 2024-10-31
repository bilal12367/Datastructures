

nums = [0,1,0,3,2,3]

def lis(nums):
    n = len(nums)
    lis1 = 0
    for i in range(n):
        temp = nums[i]
        cnt = 1
        for j in range(i, n):
            if temp < nums[j]:
                temp = nums[j]
                cnt += 1
        if cnt > lis1:
            lis1 = cnt
    
    return lis1


print(lis(nums))