from collections import defaultdict


class Solution:
    def longestSubsequence(self, arr: list[int], diff: int) -> int:
        n = len(arr)
        aux = defaultdict(int)
        for num in arr[::-1]:
            aux[num] = aux[num + diff] + 1
        return max(aux.values())


def main():
    sol = Solution()
    print('4 ===', sol.longestSubsequence(arr=[1, 2, 3, 4], difference=1))
    print('1 ===', sol.longestSubsequence(arr=[1, 3, 5, 7], difference=1))
    print('4 ===', sol.longestSubsequence(arr=[1,5,7,8,5,3,4,2,1], difference=-2))


if __name__ == '__main__':
    main()