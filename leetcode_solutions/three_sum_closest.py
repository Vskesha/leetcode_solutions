import test


def three_sum_closest(nums: list[int], target: int) -> int:
    nums.sort()
    min_dif = target - sum(nums[:3])
    ln = len(nums)
    for i in range(ln-2):
        if i != 0 and nums[i] == nums[i-1]:
            continue
        trg = target - nums[i]
        li = i + 1
        ri = ln - 1
        while li < ri:
            dif = trg - nums[li] - nums[ri]
            if abs(min_dif) > abs(dif):
                min_dif = dif
            if not dif:     # dif == 0
                return target
            elif dif > 0:   # dif > 0
                li += 1
            else:           # dif < 0
                ri -= 1
    return target - min_dif


if __name__ == '__main__':
    test.assert_equals(three_sum_closest([-1, 2, 1, -4], 1), 2)
    test.assert_equals(three_sum_closest([0, 0, 0], 1), 0)
