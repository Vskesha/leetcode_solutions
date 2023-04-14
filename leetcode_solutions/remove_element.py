import test


def remove_element1(nums: list[int], val: int) -> int:
    if not nums:
        return 0
    left = 0
    right = len(nums) - 1
    while left <= right:
        if nums[left] != val:
            left += 1
        elif nums[right] == val:
            right -= 1
        else:
            nums[left] = nums[right]
            right -= 1
    return left


def remove_element(nums: list[int], val: int) -> int:
    if not nums:
        return 0
    left = 0
    right = len(nums) - 1
    while left <= right:
        if nums[left] == val:
            nums[left] = nums[right]
            right -= 1
        else:
            left += 1
    return left



if __name__ == '__main__':
    nums = [3, 2, 2, 3]
    val = 3
    test.assert_equals(remove_element(nums, val), 2)
    print(nums)

    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    val = 2
    test.assert_equals(remove_element(nums, val), 5)
    print(nums)

    nums = [2, 2]
    val = 2
    test.assert_equals(remove_element(nums, val), 0)
    print(nums)

    nums = [2]
    val = 2
    test.assert_equals(remove_element(nums, val), 0)
    print(nums)

    nums = [1]
    val = 2
    test.assert_equals(remove_element(nums, val), 1)
    print(nums)
