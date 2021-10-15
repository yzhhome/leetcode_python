"""
    1011. 在D天内送达包裹的能力
    https://leetcode-cn.com/problems/capacity-to-ship-packages-within-d-days/
"""

from typing import List

# weights重量的货物，以cap的运载能力，D天内能否完成运输
def canFinish(weights, D, cap):
    i = 0
    for day in range(D):
        maxCap = cap
        maxCap = maxCap - weights[i]
        while maxCap >= 0:            
            i = i + 1
            # 能装下货物
            if i == len(weights):
                return True
            maxCap = maxCap - weights[i]
    return False

# 货物重量的最大值
def getMax(weights):
    return max(weights)

# 货物重量的和
def getSum(weights):
    return sum(weights)

def shipWithinDays(weights: List[int], days: int) -> int:
    # 套用二分搜索左侧边界的算法框架
    left = getMax(weights); right = getSum(weights) + 1
    while left < right:
        mid = left + (right - left) // 2
        if canFinish(weights, days, mid):
            right = mid
        else:
            left = mid + 1

    return left

if __name__ == '__main__':
    D = 5
    weights = [1,2,3,4,5,6,7,8,9,10]
    print(shipWithinDays(weights, D))