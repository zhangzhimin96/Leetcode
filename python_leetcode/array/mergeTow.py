def merge(nums1, m, nums2, n):
    mn = m + n
    m -= 1
    n -= 1
    while n >= 0:
        mn -= 1
        if m >= 0 and nums1[m] > nums2[n]:
            nums1[mn] = nums1[m]
            m -= 1
        else:
            nums1[mn] = nums2[n]
            n -= 1


if __name__ == "__main__":
    a = [1, 2, 3, 0, 0, 0]
    b = [1, 3, 5]
    merge(a, 3, b, 3)
    print(a)
