

def equalSumPartition(arr, n, sum1):
    if  n == 0:
        return
    
    if n % 2 == 0:
        equalSumPartition(arr, n//2, sum1)
        equalSumPartition(arr, )
    
    
    
def can_partition(nums, n, sum1, sum2, arr1, arr2):
    if sum1 == sum2 and len(arr1) > 0:
        return [arr1, arr2]

    if n < 0:
        return False

    res1 = can_partition(
        nums, n-1, sum1 + nums[n], sum2, arr1 + [nums[n]], arr2)
    res2 = can_partition(nums, n-1, sum1, sum2 +
                         nums[n], arr1, arr2 + [nums[n]])

    res1 = res1 or res2
    return res1
    
def equalSum(arr, n, sum1, sum2, arr1, arr2):
    if sum1 == sum2 and len(arr1) > 0:
        return [arr1, arr2]
    
    if n == 0:
        return False
    
    include_current = equalSum(arr, n - 1, sum1 + arr[n - 1], sum2, arr1 + [arr[n - 1]], arr2)
    exclude_current = equalSum(arr, n - 1, sum1 , sum2 + arr[n - 1] , arr1, arr2 + [arr[n - 1]])

    return include_current or exclude_current

def minSubsetDiff(arr, n , sum1, sum2):
    if n == 0:
        return abs(sum1 - sum2)
    
    include_current = minSubsetDiff(arr, n-1, sum1 + arr[n - 1], sum2)
    exclude_current = minSubsetDiff(arr, n-1, sum1, sum2 + arr[n - 1])

    return min(include_current , exclude_current)

if __name__ == '__main__':
    arr = [1,5,11,6]
    # print(can_partition(arr, len(arr) - 1, 0, 0, [],[]))
    # print(equalSum(arr, len(arr), 0, 0, [], []))
    arr1 = [1, 2, 3, 9]
    print(minSubsetDiff(arr1, len(arr1), 0, 0))