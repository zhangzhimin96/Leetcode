# leetcode : 21 : 合并两个有序链表


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    head = ListNode(None)
    node = head
    while l1 and l2:
        if l1.val < l2.val:
            node.next, l1 = l1, l1.next
        else:
            node.next, l2 = l2, l2.next
        node = node.next
    if l1:
        node.next = l1
    else:
        node.next = l2
    return head.next


if __name__ == "__main__":
    a = ListNode(1)
    b = ListNode(2)
    b.next = ListNode(3)

    ret = mergeTwoLists(a, b)
    print(a.next.val)
