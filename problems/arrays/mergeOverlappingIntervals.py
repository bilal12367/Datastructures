
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

intervals=[[1,2], [3, 5], [4, 6], [5, 7], [8,10], [11, 15]]

resArr = []
i = 1
while(i<len(intervals)):
    current = intervals[i]
    prev = intervals[i-1]
    if(prev[len(prev) - 1] < current[0]):
        intervals[i - 1] = prev
        if i == len(intervals) - 1:
            intervals[i] = current
    else:
        intervals[i-1] = ([prev[0], current[len(prev)-1]])
        del intervals[i]
        i -= 1
    i += 1
    

print(intervals)
    