"""
    1143. 最长公共子序列
    https://leetcode-cn.com/problems/longest-common-subsequence/
"""

import numpy as np

# text1[0..i-1] 和 text2[0..j-1]，它们的 LCS 长度是 dp[i][j]
def longestCommonSubsequence(text1: str, text2: str) -> int:
    m, n = len(text1), len(text2)

    # dp数组全部初始化为0
    dp = np.zeros(shape=(m + 1, n + 1), dtype=int)
    for i in range(m + 1):
        for j in range(n + 1):
            # 1<=i<=m,  1<=j<=n
            if i == 0 or j == 0:
                continue
            # 找到一个属于LCS中的元素
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                # 至少有一个字符不在 LCS 中
                # 取当前位置的左边和上边的 LCS                
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]


if __name__ == '__main__':
    text1 = "abcdefghijklmn"
    text2 = "aceadehjln"

    print(longestCommonSubsequence(text1, text2))