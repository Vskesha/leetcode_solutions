def min_subarr_sum(target: int, nums: list[int]) -> int:
    """This function calculates the minimal length of subarray whose sum is
    greater or equal to 'target'

    Args:
        target (int): positive integer
        nums (list[int]): array of positive integers 

    Returns:
        int: minimal length of a subarray whose sum is greater than or equal to target
    """
    start = 0
    curr_sum = 0
    min_len = len(nums) + 1
    for end in range(len(nums)):
        curr_sum += nums[end]
        while curr_sum >= target:
            min_len = min(min_len, end - start + 1)
            curr_sum -= nums[start]
            start += 1
    return 0 if min_len > len(nums) else min_len
        

if __name__ == '__main__':
    print('2 ===', min_subarr_sum(7, [2,3,1,2,4,3]))
    print('1 ===', min_subarr_sum(4, [1,4,4]))
    print('0 ===', min_subarr_sum(11, [1,1,1,1,1,1,1,1]))
    