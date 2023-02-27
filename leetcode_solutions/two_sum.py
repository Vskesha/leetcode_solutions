def two_sum(nums: list[int], target: int) -> list[int]:
    n = sorted(nums)
    l, r = 0, len(nums) - 1
    while l < r:
        s = n[l] + n[r]
        if s > target:
            r -= 1
        elif s < target:
            l += 1
        else:
            i1 = nums.index(n[l])
            i2 = nums.index(n[r])
            if i1 == i2:
                i2 = nums[i1 + 1:].index(n[r]) + i1 + 1
            return sorted([i1, i2])
    return []


if __name__ == '__main__':
    print(two_sum([2, 7, 11, 15], 9))
    print(two_sum([3, 2, 4], 6))
    print(two_sum([3, 3], 6))
    print(two_sum([9, 3, 3], 6))
