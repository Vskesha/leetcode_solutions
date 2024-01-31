from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        lt = len(temperatures)
        st, ans = [], [0] * lt
        for i, t in enumerate(temperatures):
            while st and st[-1][0] < t:
                _, pi = st.pop()
                ans[pi] = i - pi
            st.append((t, i))
        return ans


class Solution2:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        lt = len(temperatures)
        ans = [0] * lt
        st = []
        for i in range(lt - 1, -1, -1):
            t = temperatures[i]
            while st and st[-1][0] <= t:
                st.pop()
            if st:
                ans[i] = st[-1][1] - i
            st.append((t, i))
        return ans


def test():
    sol = Solution()

    print("Test 1... ", end="")
    assert sol.dailyTemperatures(temperatures=[73, 74, 75, 71, 69, 72, 76, 73]) == [
        1,
        1,
        4,
        2,
        1,
        1,
        0,
        0,
    ]
    print("OK")

    print("Test 2... ", end="")
    assert sol.dailyTemperatures(temperatures=[30, 40, 50, 60])
    print("OK")

    print("Test 3... ", end="")
    assert sol.dailyTemperatures(temperatures=[30, 60, 90]) == [1, 1, 0]
    print("OK")


if __name__ == "__main__":
    test()
