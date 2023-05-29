class Solution:

    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red, white, blue = 0, 0, len(nums) - 1

        while white <= blue:
            if nums[white] == 0:
                nums[white], nums[red] = nums[red], nums[white]
                white += 1
                red += 1
            elif nums[white] == 1:
                white += 1
            else:
                nums[white], nums[blue] = nums[blue], nums[white]
                blue -= 1
                
                
if __name__ == '__main__':
    
    sol = Solution()
    
    nums = [2,0,2,1,1,0]
    output =  [0,0,1,1,2,2]
    sol.sortColors(nums)
    print(output, '===', nums)
    
    nums = [2,0,1]
    output = [0,1,2]
    sol.sortColors(nums)
    print(output, '===', nums)
    
    nums = [1,2,0]
    output = [0, 1, 2]
    sol.sortColors(nums)
    print(output, '===', nums)