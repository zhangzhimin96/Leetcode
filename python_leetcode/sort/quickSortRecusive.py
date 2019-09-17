# 快速排序 -- 递归
def quick_sort(array, l: int, r: int):
    if l < r:
        q = partition(array, l, r)
        quick_sort(array, l, q - 1)
        quick_sort(array, q + 1, r)
    else:
        return 0


def partition(array, l, r):
    x = array[r]  # 以最后一个为中间元素
    i = l  # 中间元素的下标索引
    for j in range(l, r):
        if array[j] < x:
            array[i], array[j] = array[j], array[i]  # 把大的元素一直往后挪动到分区元素的后面
            i += 1
    array[i], array[r] = array[r], array[i]
    return i


if __name__ == "__main__":
    a = [4, 7, 2, 8, 9, 21, 1, 16]
    quick_sort(a, 0, len(a) - 1)
    print(a)
