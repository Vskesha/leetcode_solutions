class Solution:
    def putMarbles(self, weights: list[int], k: int) -> int:
        edges = sorted([weights[i] + weights[i-1]  for i in range(1, len(weights))])
        return sum(edges[-i-1] - edges[i] for i in range(k - 1))


def main():
    sol = Solution()
    print('4 ===', sol.putMarbles(weights=[1, 3, 5, 1], k=2))
    print('0 ===', sol.putMarbles(weights=[1, 3], k=2))


if __name__ == '__main__':
    main()
