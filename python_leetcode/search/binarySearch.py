# 二分查找


# 二分查找某个值，数据不重复
def binarySearch(a, v):
    if a is None:
        return -1
    l = 0
    r = len(a) - 1
    while l <= r:
        middle = l + (r - l) // 2
        if v > a[middle]:
            l = middle + 1
        elif v < a[middle]:
            r = middle - 1
        # elif middle == 0 or (a[middle-1] != a[middle]):#查找第一个
        #     return middle
        elif a[middle + 1] != a[middle]:  # 查最后第一个
            return middle
        else:
            r = middle - 1
    return -1


if __name__ == "__main__":
    a = [1, 3, 5, 5, 7, 8, 9]
    b = binarySearch(a, 5)
    print(b)
