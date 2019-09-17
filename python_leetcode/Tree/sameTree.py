# 相同的树 ： 100


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def isSameTree(p: TreeNode, q: TreeNode) -> bool:
    if p is None and q is None:
        return True
    if p is None or q is None:
        return False
    if p.val != q.val:
        return False
    # 经过上面的三步判断，可以判断当前节点是一样的，接着递归判断子节点
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)


if __name__ == "__main__":
    t1 = TreeNode(1)
    t1.left = TreeNode(2)
    t1.right = TreeNode(3)

    t2 = TreeNode(1)
    t2.left = TreeNode(2)
    t2.right = TreeNode(3)

    print(isSameTree(t1, t2))
