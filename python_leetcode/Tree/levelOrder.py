# 二叉树的层次遍历：102（从上往下遍历打印）
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 非递归
def levelOrder(root: TreeNode):
    if root is None:
        return []
    res = []
    queue = [root]  # 当前层的节点
    while queue:
        next_queue = []  # next_quene存放下一层的节点
        item = []
        for node in queue:
            if node:
                item.append(node.val)
                next_queue.append(node.left)
                next_queue.append(node.right)
        if item:
            res.append(item)  # 将当前层的数据插入res
            # res.insert(0, item)# 从最后一层遍历    leetcode:107
        queue = next_queue
    return res


if __name__ == "__main__":
    t1 = TreeNode(1)
    t1.left = TreeNode(2)
    t1.right = TreeNode(3)
    t1.right.left = TreeNode(4)

    print(levelOrder(t1))
