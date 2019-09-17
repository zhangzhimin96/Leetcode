# 选择排序，将元素分为已排序区间和未排序区间，每次从未排序区间选择最小的元素，将其插入到已排序区间的末尾


def selectSort(a, n):
    if a is None or n == 1:
        return
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):  # 找到最小元素
            if a[j] < a[min_index]:
                min_index = j
        if i != min_index:  # 若是假定的第一个就是最小值，就没有必要交换了
            a[min_index], a[i] = a[i], a[min_index]


if __name__ == "__main__":
    # a = [4,7,2,8,21,9]
    a = [7, 2, 3, 4, 5]
    selectSort(a, len(a))
    print(a)
