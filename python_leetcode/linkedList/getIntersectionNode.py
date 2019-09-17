# 查找单链表相交的起始节点 ： 160
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def getIntersectionNode(headA, headB):
    """
    :type head1, head1: ListNode
    :rtype: ListNode
    """
    p,q = headA,headB
    while p!=q:
        p = p.next if p else headB
        q = q.next if q else headA
    return p