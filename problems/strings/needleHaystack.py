


def findFirstOccurence(needle, haystack):
    ind = -1
    for i in range(len(haystack) - len(needle) + 1):
        if needle == haystack[i:i + len(needle)]:
            ind = i
            break
    return ind
        


print(findFirstOccurence("sad", "sadbutsad"))