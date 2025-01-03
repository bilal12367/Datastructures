
test_cases = [
    ([[1, 3], [2, 6], [8, 10], [15, 18]], [[1, 6], [8, 10], [15, 18]]),
    ([[1, 4], [2, 3]], [[1, 4]]),
    ([[1, 5], [6, 8], [3, 7]], [[1, 8]]),
    ([[1, 10], [2, 6], [8, 10], [15, 18]], [[1, 10], [15, 18]]),
    ([[1, 3], [4, 5], [6, 8]], [[1, 3], [4, 5], [6, 8]]),
    ([[1, 2], [3, 5], [6, 7], [8, 10]], [[1, 2], [3, 5], [6, 7], [8, 10]]),
    ([[1, 2], [2, 3], [4, 5], [6, 7]], [[1, 3], [4, 5], [6, 7]]),
    ([[1, 4], [5, 6], [7, 8]], [[1, 4], [5, 6], [7, 8]]),
    ([[1, 4], [3, 6], [7, 8], [10, 12]], [[1, 6], [7, 8], [10, 12]]),
    ([[1, 5], [5, 10], [10, 15]], [[1, 15]]),
    ([[1, 4], [6, 9], [2, 5], [12, 15], [14, 18]], [[1, 5], [6, 9], [12, 18]]),
    ([[1, 2], [2, 3], [3, 4], [4, 5]], [[1, 5]]),
    ([[5, 10], [1, 3], [2, 4], [8, 12]], [[1, 4], [5, 12]]),
    ([[1, 2], [3, 4], [5, 6]], [[1, 2], [3, 4], [5, 6]]),
    ([[1, 100], [2, 5], [4, 8], [10, 15], [20, 30]], [[1, 100]])
]

def mergeIntervals(intervals):
    intervals.sort()
    prev = intervals[0]
    res = [prev]
    for i in intervals[1:]:
        curr = i
        if curr[0] <= prev[1]:
            prev[1] = max(curr[1],prev[1])
        else:
            res.append(curr)
            prev = curr
    return res

for i in test_cases:
    res = mergeIntervals(i[0])
    assert res == i[1], "List is equal"
print("Tests Passed")