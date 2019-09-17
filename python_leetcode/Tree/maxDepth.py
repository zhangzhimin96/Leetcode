# 二叉树的最大深度：104
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 递归
def maxDepthRecursion(root: TreeNode) -> int:
    if root is None:
        return 0
    else:
        left_length = maxDepthRecursion(root.left)
        right_length = maxDepthRecursion(root.right)
        return max(left_length, right_length) + 1


# 非递归
def maxDepth(root: TreeNode) -> int:
    if not root:
        return 0
    queue = []
    visited = []  # 图访问的话要记录已经被访问的节点
    queue.append(root)
    length = 0
    while queue:
        length += 1  # 遍历一次，深度加1
        for i in queue:
            node = queue.pop(0)
            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)
    return length


if __name__ == "__main__":
    t1 = TreeNode(1)
    t1.left = TreeNode(2)
    t1.right = TreeNode(3)
    t1.left.left = TreeNode(4)

    print(maxDepth(t1))
