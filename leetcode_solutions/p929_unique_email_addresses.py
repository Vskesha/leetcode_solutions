from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        es = set()
        for email in emails:
            p = email.split("@")
            p[0] = p[0].split("+")[0].replace(".", "")
            es.add("@".join(p))
        return len(es)


class Solution2:
    def numUniqueEmails(self, emails: List[str]) -> int:
        es = set()

        for email in emails:
            local, domain = email.split("@", 1)
            pi = local.find("+")
            if pi != -1:
                local = local[:pi]
            local = local.replace(".", "")
            es.add(local + "@" + domain)

        return len(es)


def test():
    sol = Solution()

    print("Test 1... ", end="")
    assert (
        sol.numUniqueEmails(
            emails=[
                "test.email+alex@leetcode.com",
                "test.e.mail+bob.cathy@leetcode.com",
                "testemail+david@lee.tcode.com",
            ]
        )
        == 2
    )
    print("OK")

    print("Test 2... ", end="")
    assert (
        sol.numUniqueEmails(
            emails=["a@leetcode.com", "b@leetcode.com", "c@leetcode.com"]
        )
        == 3
    )
    print("OK")


if __name__ == "__main__":
    test()
