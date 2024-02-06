
def countOfSubsetDiff(arr, n, diff, sum1, sum2):
    
    if (sum1 - sum2) == diff:
        return 1

    if n == 0:
        return 0
    
    include_current = countOfSubsetDiff(arr, n - 1, diff, sum1 + arr[n-1], sum2)
    exclude_current = countOfSubsetDiff(arr, n - 1, diff, sum1 , sum2 +arr[n-1])
    return include_current + exclude_current

if __name__ == '__main__':
    arr =[ 1,1,2,3]
    diff = 1
    print(countOfSubsetDiff(arr, len(arr), diff, 0,0))