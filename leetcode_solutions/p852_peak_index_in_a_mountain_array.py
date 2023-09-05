class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        l, r = 0, len(arr) - 1

        while l < r:
            m = (l + r) // 2
            if arr[m] > arr[m+1]:
                r = m
            else:
                l = m + 1

        return l


def main():
    sol = Solution()
    print('1 ===', sol.peakIndexInMountainArray(arr=[0, 1, 0]))
    print('1 ===', sol.peakIndexInMountainArray(arr=[0, 2, 1, 0]))
    print('1 ===', sol.peakIndexInMountainArray(arr=[0, 10, 5, 2]))


if __name__ == '__main__':
    main()
