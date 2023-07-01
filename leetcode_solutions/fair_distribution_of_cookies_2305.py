class Solution:
    def distributeCookies(self, cookies: list[int], k: int) -> int:
        self.ans = float('inf')
        n = len(cookies)
        def distribution(curr_bag, curr_distribution):
            if curr_bag == n:
                self.ans = min(self.ans, max(curr_distribution))
                return
            val = cookies[curr_bag]
            for i in range(k):
                curr_distribution[i] += val
                distribution(curr_bag + 1, curr_distribution)
                curr_distribution[i] -= val

        distribution(0, [0] * k)
        return self.ans


def main():
    sol = Solution()
    print('31 ===', sol.distributeCookies(cookies=[8, 15, 10, 20, 8], k=2))
    print('7 ===', sol.distributeCookies(cookies=[6, 1, 3, 2, 2, 4, 1, 2], k=3))


if __name__ == '__main__':
    main()
