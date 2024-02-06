

def countOfSubsetSum(arr, n, target, subset, sets):
    # print(subset)
    if target == sum(subset):
        # print("Ans: ", subset)
        if subset not in sets:
            sets += [subset]
        countOfSubsetSum(arr, n-1, target, [], sets)

    if n <= 0:
        return 0, sets
    if (arr[n] > target):
        countOfSubsetSum(arr, n - 1, target, subset, sets)
    else:
        countOfSubsetSum(arr, n - 1, target, subset, sets)
        countOfSubsetSum(arr, n - 1, target, subset + [arr[n]], sets)
        print(sets)
        # if n == len(arr) - 1:
        #     return len(sets), sets


def count_subset_sum_recursive(nums, target, n):
    # Base cases
    if target == 0:
        return 1  # There is always one subset with sum 0 (the empty set)
    if n == 0:
        return 0  # No more elements in the set, and the target is not 0

    # Recursive cases
    # Count subsets by including the current element
    include_current = 0
    if nums[n - 1] <= target:
        include_current = count_subset_sum_recursive(
            nums, target - nums[n - 1], n - 1)

    # Count subsets by excluding the current element
    exclude_current = count_subset_sum_recursive(nums, target, n - 1)

    # Total count is the sum of counts from both cases
    return include_current + exclude_current


def countOfSubsetSum2(arr, target, n, subset, sets):
    if target == 0:
        sets += [subset]
        return subset, sets
    if n == 0:
        return False, sets

    include_current = []
    subsets_include = []
    if arr[n - 1] <= target:
        include_current, subsets_include = countOfSubsetSum2(
            arr, target - arr[n - 1], n - 1, subset + [arr[n - 1]], sets)
    exclude_current, subsets_exclude = countOfSubsetSum2(
        arr, target, n-1, subset, sets)
    if len(arr) == n:
        return len(subsets_exclude), subsets_exclude
    include_current = include_current or exclude_current
    subsets_include = subsets_include or subsets_exclude
    return include_current, subsets_include


def countOfSubsetSum3(arr, target, n, subset,sets):
    if target == 0:
        # return 1
        return subset

    if n == 0:
        # return 0
        return []

    include_current = []
    if arr[n - 1] <= target:
        include_current = countOfSubsetSum3(arr, target - arr[n - 1], n - 1 , subset + [arr[n-1]],sets)
    exclude_current = countOfSubsetSum3(arr, target, n-1, subset,sets)
    if include_current not in sets:
        sets += [include_current]
    if exclude_current not in sets:
        sets += [exclude_current]
    if n == len(arr):
        sets.remove([])
        return sets

    return include_current or exclude_current


if __name__ == '__main__':
    arr = [2, 4, 6, 8, 1, 3, 7]
    target = 18
    # print(countOfSubsetSum(arr, len(arr)-1, target, [], []))
    # print(count_subset_sum_recursive(arr, target, len(arr)))
    print(countOfSubsetSum3(arr, target, len(arr), [], []))
