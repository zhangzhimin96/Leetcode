# leetcode : 876 : 链表的中间节点


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def middleNode(self, head: ListNode) -> ListNode:
    # 解法1,放到一个数组里，然后取中间节点
    # A = [head]
    # while A[-1].next:
    #     A.append(A[-1].next)
    # return A[len(A) // 2]

    # 解法2，快慢指针法
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


if __name__ == "__main__":
    a = [1, 2, 3, 4, 5, 6]
    print(a[-1])
