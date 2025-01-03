


"""
Problem Statement:
Given an array of integers `arr` and an integer `target`, return the indices of the two numbers such that they add up to `target`.
Functionality:
- The function sorts the array.
- It uses a two-pointer technique to find two numbers in the sorted array that add up to the target.
- If such a pair is found, it returns their indices.
- If no such pair is found, it returns an empty list.
Variables:
- arr: List of integers to search within.
- target: The integer sum we are looking for.
- left: The starting index of the array.
- right: The ending index of the array.
- pairs: A list to store pairs of indices (not used in the final implementation).
- res: The result list to store the indices of the two numbers that add up to the target.
Returns:
- A list containing the indices of the two numbers that add up to the target, or an empty list if no such pair exists.
"""
# tests = [[3,2,4],[-3,4,3,90]]

arr = [2, 1 , 3, 4, 11 , 4, 6, 8, 7, 14]
def two_sum(arr, target):
    orig = arr.copy()
    arr.sort()
    l = 0
    r = len(arr) - 1
    while l < r:
        sum = arr[l] + arr[r]
        if sum < target:
            l += 1
        elif sum > target:
            r -= 1
        else:
            return [orig.index(arr[l]), orig.index(arr[r])]

def two_sum_optimal(arr, target):
    d = {}
    for ind,i in enumerate(arr):
        print(i, ind)
        sum = target - i
        if sum in d:
            return [d[sum], ind]
        d[i] = ind
print(two_sum_optimal(arr, 15))
