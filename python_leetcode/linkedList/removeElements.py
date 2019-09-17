# 移除链表元素 ： 203
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        # 虚拟节点，因为头结点也有可能是要删除的节点
        p = ListNode(val-1)
        p.next = head
        pre = p
        while pre.next:
            if pre.next.val == val:
                pre.next = pre.next.next
            else:
                pre = pre.next

        return p.next