"""
    875. 爱吃香蕉的珂珂
    https://leetcode-cn.com/problems/koko-eating-bananas/
"""

# n根香蕉以speed吃完需要的时间
def timeof(n, speed):
    return (n // speed) + (1 if n % speed > 0 else 0)

# piles堆香蕉，以speed的速度，H小时内能否吃完
def canFinish(piles, speed, H):
    # 累加吃每堆香蕉的时间
    time = 0
    for n in piles:
        time += timeof(n, speed)
    return time <= H

# 每堆香蕉根数的最大值
def getMax(piles):
    maxValue = 0
    for n in piles:
        maxValue = max(n, maxValue)
    return maxValue

def minEatingSpeed(piles, H):
    # 套用二分搜索左侧边界的算法框架
    left = 1; right = getMax(piles) + 1
    while left < right:
        mid = left + (right - left) // 2
        if canFinish(piles, mid, H):
            right = mid
        else:
            left = mid + 1

    return left

if __name__ == '__main__':
    H = 8
    piles = [3,6,7,11]
    print(minEatingSpeed(piles, H))