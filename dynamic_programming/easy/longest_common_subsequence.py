class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        return self.lcs(text1, text2, len(text1), len(text2))
    def lcs(self, t1, t2, n, m):
        if n == 0 or m == 0:
            return 0
        if t1[n - 1] == t2[m - 1]:
            return 1 + self.lcs(t1, t2, n - 1, m - 1)
        else:
            return max(self.lcs(t1, t2, n - 1, m), self.lcs(t1, t2, n, m - 1))
    
        