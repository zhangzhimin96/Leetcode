# 删除排序链表中的重复元素 ：83


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def deleteDuplicates(self, head: ListNode) -> ListNode:
    if head == None or head.next == None:
        return head
    p_node = head
    # 重点是该链表是有序的，否则得重新排序，和当前的值比较
    target = p_node.val
    while True:
        if p_node.next.val == target:
            p_node.next = p_node.next.next
        else:
            target = p_node.next.val
            p_node = p_node.next
        if p_node.next is None:
            break
    return head


if __name__ == "__main__":
    print(12)
