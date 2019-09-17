# 快速排序 --非递归
def quick_sort(array, l, r):
    if l >= r:
        return
    stack = [l, r]  # 栈里面存的是数组下标
    while stack:
        low = stack.pop(0)
        high = stack.pop(0)
        if high - low <= 0:
            continue
        x = array[high]  # 取最后一个元素为基准来进行分区
        i = low - 1
        for j in range(low, high):
            if array[j] <= x:
                i += 1
                array[i], array[j] = array[j], array[i]
        array[i + 1], array[high] = array[high], array[i + 1]
        stack.extend([low, i, i + 2, high])
        print(stack)


if __name__ == "__main__":
    a = [4, 7, 2, 8, 9, 21]
    quick_sort(a, 0, len(a) - 1)
    print(a)
