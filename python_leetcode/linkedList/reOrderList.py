# 重排链表 ： 143
# 给定一个单链表 L：L0→L1→…→Ln-1→Ln ，
# 将其重新排列后变为： L0→Ln→L1→Ln-1→L2→Ln-2→…
#
# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

# 思路为把链表分为两个部分，然后依次压入，后面的半部分需要反转链表


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


def reorderList(head: ListNode) -> None:
    """
    Do not return anything, modify head in-place instead.
    """
    if head is None or head.next is None:
        return None
    # 快慢指针，slow为中点，有两个的话为前面一个
    fast, slow = head, head
    while fast.next and fast.next.next:
        fast = fast.next.next
        slow = slow.next
    # 反转后半部分链表
    left = head
    right = reverseList(fast)
    while left and right:
        tmp1 = left.next
        tmp2 = right.next
        left.next, right.next = right, tmp1
        left, right = tmp1, tmp2


if __name__ == '__main__':
    a = ListNode(1)
    head = a
    for i in range(2, 5):
        a.next = ListNode(i)
        a = a.next

    reorderList(head)
    print(head)
