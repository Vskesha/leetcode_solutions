class Solution:
    def isMonotonic(self, nums: list[int]) -> bool:
        is_increasing = nums[-1] > nums[0]
        
        for i in range(1, len(nums)):
            if is_increasing and nums[i] < nums[i-1]:
                return False
            elif not is_increasing and nums[i] > nums[i-1]:
                return False
        return True
    
    
if __name__ == '__main__':
    sol = Solution()
    print('True ===', sol.isMonotonic(nums = [1,2,2,3]))
    print('True ===', sol.isMonotonic(nums = [6,5,4,4]))
    print('False ===', sol.isMonotonic(nums = [1,3,2]))
    