
# Should remove the overlapping Intervals

# Example 1:

# Input: intervals=[[1,3],[2,6],[8,10],[15,18]]

# Output: [[1,6],[8,10],[15,18]]

# Explanation: Since intervals [1,3] and [2,6] are overlapping we can merge them to form [1,6]
#  intervals.

# Example 2:

# Input: [[1,4],[4,5]]

# Output: [[1,5]]

# Explanation: Since intervals [1,4] and [4,5] are overlapping we can merge them to form [1,5].

def mergeIntervals(intervals):
    intervals.sort(key=lambda x: x[0])
    result = []
    for interval in intervals:
        if not result or result[-1][1] < interval[0]:
            result.append(interval)
        else:
            result[-1][1] = max(result[-1][1], interval[1])
    return result


intervals = [[1, 2], [3, 5], [4, 6], [5, 7], [8, 10], [11, 15]]
# intervals=[[1,4],[0,4]]
# intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
# intervals = [[1, 4], [0, 1]]
# intervals = [[1,4],[2,3]]
# intervals = [[1,4],[4,5]]


print(mergeIntervals(intervals))
