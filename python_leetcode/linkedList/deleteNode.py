# leetcode : 237 删除链表中的节点


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def deleteNode(node):
    """
    :type node: ListNode
    :rtype: void Do not return anything, modify node in-place instead.
    """
    # 因为无法访问想要删除节点的前一个节点，所以将要删除的节点的值替换为它后面的节点的值，然后删除要删除节点的下一个节点
    node.val, node.next = node.next.val, node.next.next

