

def minSubsetDifference(arr, n, sum1, sum2):
    if n == 0:
        return abs(sum1 -  sum2)
    
    include_current = minSubsetDifference(arr, n - 1, sum1 + arr[n-1], sum2)
    exclude_current = minSubsetDifference(arr, n - 1, sum1, sum2 + arr[n-1])

    return min(include_current, exclude_current)
    
if __name__ == '__main__':
    arr = [1, 2, 3, 9]
    print(minSubsetDifference(arr, len(arr), 0, 0))