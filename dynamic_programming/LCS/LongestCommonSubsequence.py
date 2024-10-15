
## Success in Leetcode on your own.
def longestCommonSubsequence( text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)

        t = [[-1 for _ in range(m + 1)] for _ in range(n + 1)]
        for i in range(n + 1):
              for j in range(m + 1):
                    if i == 0 or j == 0:
                        t[i][j] = 0
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if text1[j - 1] == text2[i - 1]:
                    t[i][j] = 1 + t[i - 1][j - 1]
                else:
                    t[i][j] = max(t[i][j - 1],t[i - 1][j])
        
        return t[n][m]

def longestCommonSubstring(text1: str, text2: str,count) -> int:
    m = len(text1)
    n = len(text2)
    if m == 0 or n == 0:
        return count
    
    if text1[- 1] == text2[- 1]:
        return longestCommonSubstring(text1[:-1], text2[:-1], count + 1)
    else:
        return max(count,longestCommonSubstring(text1[:-1],text2[:-1], 0), longestCommonSubstring(text1[:-1],text2, 0), longestCommonSubstring(text1,text2[:-1], 0))
    

print("Res= ", longestCommonSubstring("abcdef","abcdjedef",0))