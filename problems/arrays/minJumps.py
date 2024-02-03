
def minJumps(arr):
    jump = arr[0]
    jmpCount = 0
    i = 0
    while i < len(arr):
        if i == jump:
            print(i, ' ',jump)
            jump = i + arr[i]
            jmpCount += 1
        i+=1
    
    print(jmpCount)

minJumps([1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9])