class Solution:
    def distinctDifferenceArray(self, nums: list[int]) -> list[int]:
        n = len(nums)
        diff = [0] * n
        distinct = set()
        
        for i in range(n):
            distinct.add(nums[i])
            diff[i] = len(distinct)

        distinct.clear()
        for i in range(n-1, -1, -1):
            diff[i] -= len(distinct)
            distinct.add(nums[i])

        return diff
    
    
if __name__ == '__main__':
    sol = Solution()
    print('[-3, -1, 1, 3, 5] ===', sol.distinctDifferenceArray(nums = [1,2,3,4,5]))
    print('[-2, -1, 0, 2, 3] ===', sol.distinctDifferenceArray(nums = [3,2,3,4,2]))
      