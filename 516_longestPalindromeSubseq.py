"""
    516. 最长回文子序列
    https://leetcode-cn.com/problems/longest-palindromic-subsequence/
"""

def longestPalindromeSubseq(s):
    n = len(s)

    # dp数组全部初始化为0
    dp = [[0 for _ in range(n)] for _ in range(n)]

    #  base case
    for i in range(n):
        dp[i][i] = 1

    # 反向进行遍历
    # i: [n-2, 0]  j: [i+1, n)
    for i in range(n - 2, -1, -1):
        for j in range(i + 1, n, 1):
            
            # 相等的情况说明在回文子序列中
            # 此时i往后移，j往前移
            # dp[i][j]为dp[i + 1][j - 1]的长度
            # 再加上相等的两个字符长度
            if (s[i] == s[j]):
                dp[i][j] = dp[i + 1][j - 1] + 2

            #/ 不相等的情况说明不在回文子序列中
            # 比较s[i + 1][j]和s[i][j - 1]谁的回文子序列更长
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
    
    return dp[0][n-1]


if __name__ == '__main__':
    print(longestPalindromeSubseq("cbxabyc"))