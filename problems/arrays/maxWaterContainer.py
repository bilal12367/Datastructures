

def maxWaterContainer(height):
    i = 0
    j = len(height) - 1
    max1 = 0
    while (i < j):
        cm = min(height[i],height[j]) * (j - i)
        max1 = max(max1, cm)
        if height[i] <= height[j]:
            i += 1
        else:
            j -= 1
    return max1

print(maxWaterContainer([1,1]))