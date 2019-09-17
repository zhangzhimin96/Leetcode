# 对称二叉树 ： 101
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def isSymmetric(root: TreeNode) -> bool:
    if root is None:
        return True
    return isMirror(root.left, root.right)


def isMirror(left: TreeNode, right: TreeNode) -> bool:
    if left is None and right is None:
        return True
    if left is None or right is None:
        return False
    if left.val != right.val:
        return False
    return isMirror(left.left, right.right) and isMirror(left.right, right.left)


# class Solution:
#     def isSymmetric(self, root: TreeNode) -> bool:
#         if root == None:
#             return True
#         return self.isMirror(root.left, root.right)
#
#     def isMirror(self, left: TreeNode, right: TreeNode) -> bool:
#         if left == None and right == None:
#             return True
#         if left == None or right == None:
#             return False
#         if left.val != right.val:
#             return False
#         return self.isMirror(left.left, right.right) and self.isMirror(left.right, right.left)


if __name__ == "__main__":
    t1 = TreeNode(1)
    t1.left = TreeNode(2)
    t1.right = TreeNode(2)

    # s = Solution()
    # result = s.isSymmetric(t1)
    # print(result)
    print(isSymmetric(t1))
