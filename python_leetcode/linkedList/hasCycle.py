# 环形链表 ：141
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def hasCycle(head):
    """
    :type head: ListNode
    :rtype: bool
    """
    if head is None or head.next is None:
        return False
    fast = head
    slow = head
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            return True
    return False
