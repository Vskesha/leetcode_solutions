class Solution:
    def getAverages(self, nums: list[int], k: int) -> list[int]:
        n = len(nums)
        result = [-1] * n

        if k * 2 >= n:
            return result

        l = k * 2 + 1
        curr_sum = sum(nums[:l - 1])
        for i in range(k, n - k):
            curr_sum += nums[i + k]
            result[i] = curr_sum // l
            curr_sum -= nums[i - k]

        return result


def main():
    sol = Solution()
    print('[-1, -1, -1, 5, 4, 4, -1, -1, -1]\n', sol.getAverages(nums=[7, 4, 3, 9, 1, 8, 5, 2, 6], k=3), sep='')
    print('[100000]\n', sol.getAverages(nums=[100000], k=0), sep='')
    print('[-1]\n', sol.getAverages(nums=[8], k=100000), sep='')


if __name__ == '__main__':
    main()