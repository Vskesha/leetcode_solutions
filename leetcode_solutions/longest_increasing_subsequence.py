from bisect import bisect_left


def longest_lis(nums):
    if not nums:
        return 0
    tails = [nums[0]]
    for i in range(1, len(nums)):
        if nums[i] > tails[-1]:
            tails.append(nums[i])
        else:
            tails[bisect_left(tails, nums[i])] = nums[i]
    return len(tails)


if __name__ == '__main__':
    print('4 ===', longest_lis([10, 9, 2, 5, 3, 7, 101, 18]))
    print('4 ===', longest_lis([0, 1, 0, 3, 2, 3]))
    print('1 ===', longest_lis([7, 7, 7, 7, 7, 7, 7]))
