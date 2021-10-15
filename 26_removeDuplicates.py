"""
    26. 删除有序数组中的重复项
    https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/
"""

from typing import List

def removeDuplicates(nums: List[int]) -> int:
    n = len(nums)
    if n == 0: return 0

    # slow为慢指针, fast为快指针
    slow = 0; fast = 1
    while fast < n:
        if nums[fast] != nums[slow]:
            slow += 1
            # nums[slow]为不重复的元素
            nums[slow] = nums[fast]
        fast += 1
    return slow + 1

if __name__ == '__main__':
    nums = [0,0,1,1,1,2,2,3,3,4]
    print(removeDuplicates(nums))
