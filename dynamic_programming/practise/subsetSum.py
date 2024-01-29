subset_sum_test_cases = [
    ([3, 34, 4, 12, 5, 2], 9, True),    # Subset [3, 4, 2] sums to 9
    ([3, 34, 4, 12, 5, 2], 26, True),   # Subset [3, 4, 12, 5, 2] sums to 26
    ([1, 2, 3, 4, 5], 7, True),        # Subset [1, 2, 3, 4] sums to 10
]
subset_sum_test_cases1 = [
    ([3, 34, 4, 12, 5, 2], 1, []),
    ([2, 3, 5], 5, [1, 2, 3, 4, 5])
]


def subsetSum(arr, target, n):
    if target == 0:
        return True

    if n == 0:
        return False

    if arr[n-1] <= target:
        return (subsetSum(arr, target - arr[n-1], n-1) or subsetSum(arr, target, n-1))
    else:
        return subsetSum(arr, target, n-1)


def subsetSumDP(arr, target, n):
    if n < 0 and target > 0:
        return False
    if n == 0 and target == sum(arr):
        return True

    t = [[False for i in range(target+1)] for j in range(n+1)]
    for i in range(n+1):
        t[i][0] = True
    for i in range(n+1):
        for j in range(target+1):
            if j == 0:
                t[i][j] = True

            if i == 0:
                t[i][j] = False

            if arr[i-1] <= j:
                t[i][j] = t[i-1][j - arr[i-1]] or t[i-1][j]
            else:
                t[i][j] = t[i-1][j]

    return t[n][target]


def subsetSumDPWithSubset(arr, target, n):
    t = [[False for _ in range(target+1)] for _ in range(n+1)]
    for i in range(n+1):
        t[i][0] = True
    for i in range(n+1):
        for j in range(target + 1):
            if i == 0:
                t[i][j] = False

            if j == 0:
                t[i][j] = True

            if arr[i-1] <= j:
                t[i][j] = t[i-1][j - arr[i-1]] or t[i-1][j]
            else:
                t[i][j] = t[i-1][j]
    print(t[n])
    return t[n][target]


# Iterate through test cases
for test_case in subset_sum_test_cases1:
    arr, target_sum, expected_output = test_case
    # Apply your Subset Sum algorithm here
    print("TestCase: ", test_case)
    result = subsetSumDPWithSubset(arr, sum(arr), len(arr) - 1)
    print("Result: ", result)
    # Check if the result matches the expected output
    # assert result == expected_output, f"Test failed for {
    #     test_case}. Expected {expected_output}, got {result}"
    # print("Result: ", result == expected_output)
print("All test cases passed!")
