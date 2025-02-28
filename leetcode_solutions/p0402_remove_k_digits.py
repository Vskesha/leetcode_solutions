from functools import lru_cache


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k >= len(num):
            return "0"

        stack = []
        for n in num:
            while k and stack and n < stack[-1]:
                stack.pop()
                k -= 1
            stack.append(n)
        for _ in range(k):
            stack.pop()
        return "".join(stack).lstrip("0") or "0"


class Solution1:
    def removeKdigits(self, num: str, k: int) -> str:
        st = list()
        for n in num:
            while st and k and st[-1] > n:
                st.pop()
                k -= 1

            if st or n != "0":  # prevent leading zeros
                st.append(n)

        if k:  # not fully spent
            st = st[0:-k]

        return "".join(st) or "0"


class Solution2:
    def removeKdigits(self, num: str, k: int) -> str:
        @lru_cache
        def dp(num, k):
            if k == 0:
                return num

            if k == len(num):
                return ""

            a = num[0] + dp(num[1:], k)
            b = dp(num[1:], k - 1)

            return a if int(a) < int(b) else b

        n = dp(num, k).lstrip("0")

        return n if n else "0"


class Solution3:
    def removeKdigits(self, num: str, k: int) -> str:
        res = []
        st = 0
        li = 0  # last_investigated
        m = ""
        mp = {str(i): 0 for i in range(10)}  # digit counter

        while k > 0:
            if st + k >= len(num):
                st = len(num)
                break

            # m = min(num[st:st+k+1], key=int)
            # This takes the most time. Need to improve
            for i in range(li, st + k + 1):
                mp[num[i]] += 1

            li = st + k + 1
            for i in range(10):
                if mp[str(i)] > 0:
                    m = str(i)
                    break

            while num[st] != m:
                mp[num[st]] -= 1
                st += 1
                k -= 1

            res.append(num[st])
            mp[num[st]] -= 1
            st += 1

        res += num[st:]
        res = "".join(res)
        res = res.lstrip("0")

        return res if res else "0"


def test():
    sol = Solution()

    print("Test 1... ", end="")
    assert sol.removeKdigits(num="1432219", k=3) == "1219"
    print("OK")

    print("Test 2... ", end="")
    assert sol.removeKdigits(num="10200", k=1) == "200"
    print("OK")

    print("Test 3... ", end="")
    assert sol.removeKdigits(num="10", k=2) == "0"
    print("OK")


if __name__ == "__main__":
    test()
