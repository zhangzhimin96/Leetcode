# 插入排序
# 思想：将数据分为已排序区间和未排序区间，每次从未排序区间中取一个元素，在已排序区间合适的位置插入，已排序区间一直是有序的


def insertSort(a, n):
    if a is None or n == 1:
        return
    for i in range(1, n):  # 分成两个区间，刚开始第一个元素为一个区间，其他元素为一个区间
        now = a[i]  # 将要插入的元素
        insert = i - 1  # 插入的位置
        for j in range(i - 1, -1, -1):
            if a[j] > now:
                a[j + 1] = a[j]  # 将元素往后移,j位置就是要插入的位置（原地排序）
                insert = j
            else:
                break
        a[insert] = now  # 将元素插入指定位置


if __name__ == "__main__":
    # a = [4,7,2,8,21,9]
    a = [7, 2, 3, 4, 5]
    insertSort(a, len(a))
    print(a)
