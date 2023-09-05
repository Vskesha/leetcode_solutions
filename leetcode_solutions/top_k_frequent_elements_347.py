
def topKFrequent(nums: list[int], k: int) -> list[int]:
    
    vals = dict()
    for n in nums:
        if n in vals:
            vals[n] += 1
        else:
            vals[n] = 1

    result = [0] * k
    for i in range(k):
        max_count = 0
        for k, c in vals.items():
            if c > max_count:
                max_count = c
                result[i] = k
        del vals[result[i]]

    return result 


if __name__ == '__main__':
    print('[1, 2] ===', topKFrequent(nums = [1,1,1,2,2,3], k = 2))
    print('[1] ===', topKFrequent(nums = [1], k = 1))
    