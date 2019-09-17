# leetcode : 234 : 回文链表判断
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None or head.next is None:
            return True
        target = []
        while head:
            target.append(head.val)
            head = head.next
        p = (len(target) - 1) // 2 + 1
        q = (len(target)) // 2
        # [::-1] 表示列表的转置，逆序
        return target[0:p] == target[q:len(target)][::-1]


if __name__ == "__main__":
    print(5/2)
