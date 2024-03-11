from collections import Counter


class Solution:
    def customSortString(self, order: str, s: str) -> str:
        order_dict = {ch: i for i, ch in enumerate(order)}
        return "".join(sorted(s, key=lambda ch: order_dict.get(ch, 30)))


class Solution1:
    def customSortString(self, order: str, s: str) -> str:
        cnt = Counter(s)
        ans = ""
        for ch in order:
            ans += ch * cnt[ch]
            del cnt[ch]
        for ch in cnt:
            ans += ch * cnt[ch]
        return ans


class Solution2:
    def customSortString(self, order: str, s: str) -> str:
        ids = {c: i for i, c in enumerate(order)}
        lst = list(s)
        lst.sort(key=lambda c: ids.get(c, -1))
        return "".join(lst)


def verify_sequence(sorted_str: str, order: str) -> bool:
    common = set(sorted_str) & set(order)
    sorted_list = []
    for c in sorted_str:
        if c not in sorted_list and c in common:
            sorted_list.append(c)
    order_list = [c for c in order if c in common]
    return sorted_list == order_list


def test_custom_sort_string():
    sol = Solution()

    print("Test 1... ", end="")
    assert verify_sequence(
        sorted_str=sol.customSortString(order="cba", s="abcd"), order="cba"
    )
    print("OK")

    print("Test 2... ", end="")
    assert verify_sequence(
        sorted_str=sol.customSortString(order="bcafg", s="abcd"),
        order="bcafg",
    )
    print("OK")


if __name__ == "__main__":
    test_custom_sort_string()
