# 冒泡排序
#   冒泡排序思想（升序为例）：每一次冒泡排序，通过交换元素，将大的元素往后面移动，每次冒泡结果都是可以通过一个哨兵来标识冒泡是否结束。
#   时间复杂度：O(n2)  最好时间复杂度O(n) 最差时间复杂度(O(n2))
#   空间复杂度：O(1)->原地排序
#   稳定的排序算法
# a 数组
# n 数组长度


def bubbleSort(a, n):
    if a is None or n == 1:
        return None
    for i in range(n):
        flag = False  # 哨兵标识是否还要进行下一次冒泡排序
        for j in range(n - i - 1):  # 每次冒泡将最大的元素放到正确的位置
            if a[j] > a[j + 1]:
                a[j], a[j+1] = a[j+1], a[j]
                flag = True  # 有元素交换则将哨兵标识为true
        if not flag:  # 标示所有元素已经是有序的，不需要进行下一轮冒泡了
            break


if __name__ == "__main__":
    a = [4, 7, 2, 8, 21, 9]
    bubbleSort(a, len(a))
    print(a)
