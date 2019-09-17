# 归并排序


def merge_sort_c(data_list, p, q):
    """
    递归调用
    """
    # 退出条件
    if p + 1 >= q:  # 只有两个元素的时候退出
        return
    else:
        r = (p + q) // 2  # 中间位置下标
        merge_sort_c(data_list, p, r)
        merge_sort_c(data_list, r, q)
        merge(data_list, p, r, q)  # 将data_list[p:r] 与 data_list[r:q] 按顺序归并到 data_list 相应位置


def merge(data_list, p, r, q):
    """
    归并函数
    例如 data_list[p:q] = [...,1,4,2,3,...]
    data_list[p:r] = [1,4]
    data_list[r:q] = [2,3]
    tmp = [1,2,3,4]
    归并后 data_list[p:q] = [...,1,2,3,4,...]
    """
    tmp = []
    i = p
    j = r
    while i < r and j < q:
        if data_list[i] <= data_list[j]:
            tmp.append(data_list[i])
            i += 1
        else:
            tmp.append(data_list[j])
            j += 1

    while i < r:
        tmp.append(data_list[i])
        i += 1

    while j < q:
        tmp.append(data_list[j])
        j += 1
    # 将 tmp 数据复制到 data_list
    # for tmp_index, index in enumerate(range(p, q)):
    #     data_list[index] = tmp[tmp_index]
    for m, n in enumerate(tmp):
        data_list[p+m] = tmp[m]


if __name__ == "__main__":
    a = [4, 7, 2, 8, 9, 21]
    merge_sort_c(a, 0, len(a) - 1)
    print(a)
