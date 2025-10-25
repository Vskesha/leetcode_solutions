from functools import lru_cache
from heapq import heappop, heappush
from itertools import pairwise


class Solution:
    def strongPasswordChecker(self, password: str) -> int:

        plen = len(password)
        if plen < 4:
            return 6 - plen

        ans = 3 - (
            int(any(ch.islower() for ch in password))
            + int(any(ch.isupper() for ch in password))
            + int(any(ch.isdigit() for ch in password))
        )

        if plen < 6:
            return max(6 - plen, ans)

        groups = [1]
        for a, b in pairwise(password):
            if a == b:
                groups[-1] += 1
            elif groups[-1] < 3:
                groups[-1] = 1
            else:
                groups.append(1)
        if groups[-1] < 3:
            groups.pop()

        for _ in range(ans):
            if groups:
                mg, mi = max((g, j) for j, g in enumerate(groups))
                if mg < 6:
                    groups.pop(mi)
                else:
                    groups[mi] -= 3
            else:
                break

        if plen > 20:
            to_del = plen - 20
            ans += to_del
            while groups and to_del:
                i = min(range(len(groups)), key=lambda x: groups[x] % 3)
                if groups[i] == 3:
                    groups.pop(i)
                else:
                    groups[i] -= 1
                to_del -= 1

        ans += sum(g // 3 for g in groups)
        return ans


# difficult dp solution
class Solution1:
    def strongPasswordChecker(self, password: str) -> int:
        CHARS = "abAB01"
        LP = len(password)

        def nmask(mask, ch):  # REWRITE
            if ch.islower():
                mask |= 1
            elif ch.isupper():
                mask |= 2
            elif ch.isdigit():
                mask |= 4
            return mask

        def nrep(rep, ch):
            return rep + ch if rep and rep[-1] == ch else ch

        @lru_cache(None)
        def dp(ln, pos, mask, rep) -> int:

            if ln > 20 or len(rep) > 2:
                return 100

            if pos == LP:
                if ln > 5 and mask == 7:
                    return 0
                return 100

            return min(
                dp(
                    ln + 1,
                    pos + 1,
                    nmask(mask, password[pos]),
                    nrep(rep, password[pos]),
                ),
                1 + dp(ln, pos + 1, mask, rep),
                1
                + min(
                    dp(ln + 1, pos + 1, nmask(mask, ch), nrep(rep, ch))
                    for ch in CHARS
                ),
                1
                + min(
                    dp(ln + 1, pos, nmask(mask, ch), nrep(rep, ch))
                    for ch in CHARS
                ),
            )

        return dp(0, 0, 0, "")


class Solution2:
    def strongPasswordChecker(self, password: str) -> int:
        ans = 0
        plen = len(password)

        has_lower = any(ch.islower() for ch in password)
        has_upper = any(ch.isupper() for ch in password)
        has_digit = any(ch.isdigit() for ch in password)
        without = [1 - int(has_lower), 1 - int(has_upper), 1 - int(has_digit)]

        if plen < 6:
            to_add = 6 - plen
            ans += max(to_add, sum(without))
            return ans

        groups = [1]
        for a, b in pairwise(password):
            if a == b:
                groups[-1] += 1
            else:
                groups.append(1)
        groups = [g for g in groups if g > 2]

        for i in range(3):
            if groups and without[i]:
                ans += 1
                without[i] = 0
                mg, mi = max((g, j) for j, g in enumerate(groups))
                if mg < 6:
                    groups.pop(mi)
                else:
                    groups[mi] -= 3

        if plen > 20:
            to_del = plen - 20
            ans += to_del

            while groups and to_del:
                _, i = min((g % 3, i) for i, g in enumerate(groups))
                if groups[i] == 3:
                    groups.pop(i)
                else:
                    groups[i] -= 1
                to_del -= 1

        ans += sum(g // 3 for g in groups)
        ans += sum(without)
        return ans


class Solution3:
    def strongPasswordChecker(self, password: str) -> int:
        plen = len(password)
        if plen < 4:
            return 6 - plen

        without = [1, 1, 1]
        for i, func in enumerate((str.islower, str.isupper, str.isdigit)):
            for ch in password:
                if func(ch):
                    without[i] = 0
                    break

        if plen < 6:
            return max(6 - plen, sum(without))

        ans = 0
        grheap, st = [], 0
        for i in range(1, plen):
            if password[i] != password[i - 1]:
                if i - st > 2:
                    heappush(grheap, i - st)
                st = i
        if plen - st > 2:
            heappush(grheap, plen - st)

        for i in range(3):
            if grheap and without[i]:
                ans += 1
                without[i] = 0
                mg = grheap.pop()
                if mg > 5:
                    heappush(grheap, mg - 3)

        ans += sum(without)

        if plen < 20:
            ans += sum(g // 3 for g in grheap)
            return ans

        to_del = plen - 20
        ans += to_del

        remgr = []
        for g in grheap:
            heappush(remgr, (g % 3, g))

        for _ in range(to_del):
            if not remgr:
                break
            _, g = heappop(remgr)
            if g != 3:
                g -= 1
                heappush(remgr, (g % 3, g))

        ans += sum(g // 3 for r, g in remgr)
        return ans


def test():
    sol = Solution()

    print("Test 1... ", end="")
    assert sol.strongPasswordChecker(password="a") == 5
    print("OK")

    print("Test 2... ", end="")
    assert sol.strongPasswordChecker(password="aA1") == 3
    print("OK")

    print("Test 3... ", end="")
    assert sol.strongPasswordChecker(password="1337C0d3") == 0
    print("OK")

    print("Test 4... ", end="")
    assert sol.strongPasswordChecker(password="bbaaaaaaaaaaaaaaacccccc") == 8
    print("OK")

    print("Test 5... ", end="")
    assert sol.strongPasswordChecker(password="ABABABABABABABABABAB1") == 2
    print("OK")


if __name__ == "__main__":
    test()
