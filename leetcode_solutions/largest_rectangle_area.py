class Solution:
    def largestRectangleArea(self, bars: list[int]) -> int:
        st, res = [], 0
        for bar in bars + [-1]:  # add -1 to have an additional iteration
            step = 0
            while st and st[-1][1] >= bar:
                w, h = st.pop()
                step += w
                res = max(res, step * h)
            st.append((step + 1, bar))
        return res


if __name__ == '__main__':
    sol = Solution()
    print('10 ===', sol.largestRectangleArea([2, 1, 5, 6, 2, 3]))
    print('4 ===', sol.largestRectangleArea([2, 4]))
