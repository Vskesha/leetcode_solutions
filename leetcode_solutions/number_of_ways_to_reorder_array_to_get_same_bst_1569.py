from math import comb


class Solution:
    @staticmethod
    def num_of_ways_bst(nums: list[int]) -> int:

        def num_of_ways(arr: list) -> int:

            n = len(arr)
            if n < 3:
                return 1

            left_arr, right_arr, root = [], [], arr[0]
            for i in range(1, n):
                if arr[i] < root:
                    left_arr.append(arr[i])
                else:
                    right_arr.append(arr[i])

            left_ways = num_of_ways(left_arr)
            right_ways = num_of_ways(right_arr)
            combs = comb(n - 1, len(left_arr))

            return combs * left_ways * right_ways % 1000000007

        return num_of_ways(nums) - 1