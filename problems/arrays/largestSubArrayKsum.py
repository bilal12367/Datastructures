# arr = [6, -2, 2, -8, 1, 7, 4]
str1 = "-776 794 387 -648 363 691 764 -539 -171 -210 -566 783 -861 68 930 -21 -68 394 -10 -228 422 785 199 -314 -412 -90 -955 863 -995 306 85 337 847 314 125 583 815 435 -42 -86 -275 -787 -402 755 933 -675 -738 -225 -93 796 -433 -466 98 -316 -651 -300 -285 866 445 441 32 98 482 710 568 -496 587 307 220 -527 733 504 271 -707 341 797 619 847 922 380 -763 -840 -192 -33"
arr2 = str1.split()
for i in range(len(arr2)):
    arr2[i] = int(arr2[i])
arr = [6, -2, 2, -8, 1, 7, 4]



targetSum = 0
max = 0
def largestSubArrayKSum(arr, targetSum):
    n = len(arr) - 1
    i = 0
    max = 0
    j = i + 1
    if sum(arr) == targetSum:
        max = len(arr)
    else:
        while(j<=n):
            print(arr[i:j])
            currentSum = sum(arr[i:j])
            if currentSum == targetSum:
                temp = len(arr[i:j])
                if temp > max:
                    max = temp
                j += 1
            elif currentSum > targetSum:
                i += 1
            elif currentSum < targetSum:
                j += 1
    return max

print(largestSubArrayKSum(arr2, targetSum))