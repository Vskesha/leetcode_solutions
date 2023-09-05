import test


def four_sum(nums: list[int], target: int) -> list[list[int]]:
    result = []
    nums.sort()
    ln = len(nums)
    for i in range(ln-3):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        for j in range(i+1, ln-2):
            if j > i + 1 and nums[j] == nums[j-1]:
                continue
            trg = target - nums[i] - nums[j]
            li = j + 1
            ri = ln - 1
            while li < ri:
                sm = nums[li] + nums[ri]
                if sm > trg:
                    ri -= 1
                elif sm < trg:
                    li += 1
                else:
                    result.append([nums[i], nums[j], nums[li], nums[ri]])
                    li += 1
                    while li < ln and nums[li] == nums[li-1]:
                        li += 1
    return result


if __name__ == '__main__':
    nums = [1, 0, -1, 0, -2, 2]
    target = 0
    output = [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
    test.assert_equals(four_sum(nums, target), output)
    nums = [2, 2, 2, 2, 2, 2]
    target = 8
    output = [[2, 2, 2, 2]]
    test.assert_equals(four_sum(nums, target), output)

    test.assert_equals(four_sum([-2,-1,-1,1,1,2,2], 0), [[-2,-1,1,2],[-1,-1,1,1]])