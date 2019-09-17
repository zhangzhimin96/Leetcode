# leetcode 1
# 给定 nums = [2, 7, 11, 15], target = 9
#
# 因为 nums[0] + nums[1] = 2 + 7 = 9
# 所以返回 [0, 1]


def twoSum(nums, target):
    hashmap = {}
    for i, num in enumerate(nums):
        if hashmap.get(target - num) is not None:
            return [i, hashmap.get(target - num)]
        hashmap[num] = i  # 这句不能放在if语句之前，解决list中有重复值或target-num=num的情况


if __name__ == "__main__":
    a = [1, 2, 3, 4, 5, 6, 7]
    print(twoSum(a, 6))
