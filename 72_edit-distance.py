"""
    72. 编辑距离
    https://leetcode-cn.com/problems/edit-distance/
"""

# 动态规划备忘录解法
def minDistance_memo(word1, word2):

    #保存之前计算过的
    memo = dict()

    def dp(i, j):
        # 先查之前计算过的
        if (i, j) in memo:
            return memo[(i, j)]
            
        # base case
        # i走完j还没走完，把word2中剩下的都插入到word1中
        if i == -1: return j + 1

        # j走完i还没走完，把word1中剩下的都删除
        if j == -1: return i + 1

        # 两个字符相同，各自向前移动一个字符
        if word1[i] == word2[j]:
            memo[(i, j)] = dp(i - 1, j - 1)
        else:
            # 插入: dp[i][j - 1] 插入word2中的一个字符，j前移1
            # 删除: dp[i - 1][j] 删除word1中的一个字符，i前移1
            # 替换: dp[i - 1][j - 1] word1和word2中的字符进替换，i和j都前移1
            # 每次前移操作次数加1            
            memo[(i, j)] = min(dp(i, j - 1), dp(i - 1, j), dp(i - 1, j - 1)) + 1
        return memo[(i, j)]

    return dp(len(word1) - 1, len(word2) - 1)    


# 动态规划DP Tabel解法
def minDistance(word1, word2):
    l1, l2 = len(word1), len(word2)

    # dp初始化为全0的l1 * l2列表
    dp = [[0 for _ in range(l2 + 1)] for _ in range(l1 + 1)]

    #第0列初始化为[0, l1]
    for i in range(l1 + 1):
        dp [i][0] = i
    
    #第0行初始化为[0, l2]
    for j in range(l2 + 1):
        dp[0][j] = j

    for i in range(1, l1 + 1):
        for j in range(1, l2 + 1):
            # 两个字符相同，各自向前移动一个字符
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j -1]
            else:
                # 插入: dp[i][j - 1] 插入word2中的一个字符，j前移1
                # 删除: dp[i - 1][j] 删除word1中的一个字符，i前移1
                # 替换: dp[i - 1][j - 1] word1和word2中的字符进替换，i和j都前移1
                # 每次前移操作次数加1
                dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1

    return dp[l1][l2]

if __name__ == '__main__':
    word1 = "horse"
    word2 = "ros"
    print(minDistance(word1, word2))
    print(minDistance_memo(word1, word2))