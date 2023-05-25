class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        self.nums = sorted(nums, reverse=True)[:k]
        self.k = k

    def add(self, val: int) -> int:
        if not self.nums:
            self.nums.append(val)

        if val > self.nums[-1] or len(self.nums) < self.k:
            l, r = 0, len(self.nums)
            while l < r:
                mid = (l + r) // 2
                if self.nums[mid] >= val:
                    l = mid + 1
                else:
                    r = mid
            self.nums.insert(l, val)
            while len(self.nums) > self.k:
                self.nums.pop()
        return self.nums[-1]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)


if __name__ == '__main__':
    # Input = ["KthLargest", "add", "add", "add", "add", "add"]
    # Params = [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
    # Output = [None, 4, 5, 5, 8, 8]
    
    Input = ["KthLargest","add","add","add","add","add"]
    Params = [[2,[0]],[-1],[1],[-2],[-4],[3]]
    Output = [None,-1,0,0,0,1]
    
    print(Output, end=' === [')
    ob = None
    for command, param in zip(Input, Params):
        if command == 'KthLargest':
            ob = KthLargest(*param)
            print('None', end='')
        else:
            print(',', ob.add(param[0]), end='')
    print(']') 
            