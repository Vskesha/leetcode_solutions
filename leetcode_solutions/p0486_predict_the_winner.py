from functools import lru_cache


class Solution:
    def PredictTheWinner(self, nums: list[int]) -> bool:

        @lru_cache(None)
        def first_turn(left, right):
            if left == right:
                return nums[left]
            return max(
                second_turn(left + 1, right) + nums[left],
                second_turn(left, right - 1) + nums[right],
            )

        @lru_cache(None)
        def second_turn(left, right):
            if left == right:
                return -nums[left]
            return min(
                first_turn(left + 1, right) - nums[left],
                first_turn(left, right - 1) - nums[right],
            )

        return first_turn(0, len(nums) - 1) >= 0


class Solution2:
    def PredictTheWinner(self, nums: list[int]) -> bool:

        @lru_cache(None)
        def score(left: int, right: int, turn: bool) -> int:

            if left == right:
                return nums[left] if turn else -nums[left]

            if turn:
                return max(
                    score(left + 1, right, False) + nums[left],
                    score(left, right - 1, False) + nums[right],
                )

            return min(
                score(left + 1, right, True) - nums[left],
                score(left, right - 1, True) - nums[right],
            )

        return score(0, len(nums) - 1, True) >= 0


def main():
    sol = Solution()
    print("False ===", sol.PredictTheWinner(nums=[1, 5, 2]))
    print("True ===", sol.PredictTheWinner(nums=[1, 5, 233, 7]))


if __name__ == "__main__":
    main()
