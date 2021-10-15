"""
    83. 删除排序链表中的重复元素
    https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list/
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteDuplicates(head: ListNode):
    if head == None: return None

    # slow为慢指针，fast为快指针
    slow = head
    fast = head.next

    while (fast != None):
        if fast.val != slow.val:
            slow.next = fast
            slow = slow.next
        fast = fast.next

    # 断开与后面重复元素的连接
    slow.next = None
    return head   
