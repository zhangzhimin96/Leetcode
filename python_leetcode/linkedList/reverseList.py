# 反转链表 ： 206
# 定义三个指针，pre，cur，next，移动三个指针的位置
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def reverseList(head: ListNode) -> ListNode:
    if head is None:
        return head
    pre = None
    cur = head
    while cur:
        next = cur.next
        cur.next = pre
        # 下面这两步顺序不能调换
        pre = cur
        cur = next
    return pre
