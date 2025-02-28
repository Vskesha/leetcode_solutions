from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []
        ls = len(s)
        if ls < 4:
            return []

        def not_valid_num(num) -> bool:
            return (len(num) > 1 and num.startswith("0")) or (
                len(num) > 2 and int(num) > 255
            )

        for i in range(1, min(4, ls - 2)):
            n1 = s[:i]
            if not_valid_num(n1):
                continue
            for j in range(i + 1, min(i + 4, ls - 1)):
                n2 = s[i:j]
                if not_valid_num(n2):
                    continue
                for k in range(j + 1, min(j + 4, ls)):
                    n3 = s[j:k]
                    if not_valid_num(n3):
                        continue
                    n4 = s[k:]
                    if not_valid_num(n4):
                        continue
                    ans.append(".".join((n1, n2, n3, n4)))

        return ans


class Solution1:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []
        ls = len(s)
        if ls < 4:
            return []

        def valid_nums(nums):
            for num in nums:
                if len(num) > 1 and num.startswith("0"):
                    return False
                if len(num) > 2 and int(num) > 255:
                    return False
            return True

        nums = []
        for i in range(1, min(4, ls - 2)):
            nums.append(s[:i])
            for j in range(i + 1, min(i + 4, ls - 1)):
                nums.append(s[i:j])
                for k in range(j + 1, min(j + 4, ls)):
                    nums.append(s[j:k])
                    nums.append(s[k:])
                    if valid_nums(nums):
                        ans.append(".".join(nums))
                    nums.pop()
                    nums.pop()
                nums.pop()
            nums.pop()
        return ans


class Solution2:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []
        ls = len(s)
        if ls < 4:
            return []

        def dfs(pref: str, i: int, remain: int):
            if not remain:
                if s[i] == "0" and ls - i > 1:
                    return
                tail = s[i:]
                if 0 <= int(tail) < 256:
                    ans.append(pref + tail)
                return

            if s[i] == "0":
                dfs(pref + "0.", i + 1, remain - 1)
                return

            mdcu = ls - i - remain
            for j in range(1, min(3, mdcu) + 1):
                num = s[i : i + j]
                if 0 <= int(num) < 256:
                    dfs(pref + num + ".", i + j, remain - 1)

        dfs("", 0, 3)
        return ans


def test():
    sol = Solution()

    print("Test 1... ", end="")
    assert sorted(sol.restoreIpAddresses(s="25525511135")) == sorted(
        ["255.255.11.135", "255.255.111.35"]
    )
    print("OK")

    print("Test 2... ", end="")
    assert sorted(sol.restoreIpAddresses(s="0000")) == sorted(["0.0.0.0"])
    print("OK")

    print("Test 3... ", end="")
    assert sorted(sol.restoreIpAddresses(s="101023")) == sorted(
        ["1.0.10.23", "1.0.102.3", "10.1.0.23", "10.10.2.3", "101.0.2.3"]
    )
    print("OK")


if __name__ == "__main__":
    test()
