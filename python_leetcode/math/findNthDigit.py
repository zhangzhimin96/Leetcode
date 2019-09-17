# leetcode 400
# 在无限的整数序列 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...中找到第 n 个数字。


def findNthDigit(n):
    k = 0
    count = 0

    while count < n:
        k += 1  # 数字位于几位数
        count += 9 * 10 ** (k - 1) * k  # 前面k位数的数字数量
    # clip_num = n - count + 9 * 10 ** (k - 1) * k  # 表示位于当前位数的第几位
    clip_num = int(n - 9 * 10 ** (k - 2) * (k - 1))  # 表示位于当前位数的第几位

    k_num = (clip_num - 1) // k
    k_end = (clip_num - 1) % k
    num = 10 ** (k - 1) + k_num
    return int(str(num)[k_end])


if __name__ == "__main__":
    print(findNthDigit(6))
