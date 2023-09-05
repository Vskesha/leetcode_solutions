class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        result = [[1]]
        
        if numRows == 1:
            return result
        
        for i in range(2, numRows + 1):
            prev = result[-1]
            curr = [1] * i
            for j in range(1, i - 1):
                curr[j] = prev[j] + prev[j-1]
            result.append(curr)
        return result
    

if __name__ == '__main__':
    sol = Solution()
    print(sol.generate(6))
    print(sol.generate(1))