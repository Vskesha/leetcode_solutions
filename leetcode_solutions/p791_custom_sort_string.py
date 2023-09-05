class Solution:
    def customSortString(self, order: str, s: str) -> str:
        ids = {c: i for i, c in enumerate(order)}
        lst = list(s)
        lst.sort(key=lambda c: ids.get(c, -1))
        return ''.join(lst)


def main():
    sol = Solution()
    print('cbad ===', sol.customSortString(order="cba", s="abcd"))
    print('cbad ===', sol.customSortString(order="cbafg", s="abcd"))


if __name__ == '__main__':
    main()
