class Solution:
    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:

        accs = []
        for account in accounts:
            name = account[0]
            emails = set(account[1:])
            accs.append([name, emails])

        la = len(accs)
        changes = True
        while changes:
            changes = False
            for i in range(la):
                if not accs[i]:
                    continue
                name1, emails1 = accs[i]
                for j in range(i + 1, la):
                    if accs[j]:
                        name2, emails2 = accs[j]
                        if name1 == name2 and emails1.intersection(emails2):
                            emails1.update(emails2)
                            accs[j] = []
                            changes = True

        result = []
        for acc in accs:
            if acc:
                name, emails = acc
                result.append([name] + sorted(list(emails)))

        return result


def test():
    sol = Solution()
    print(
        sol.accountsMerge(
            accounts=[
                ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
                ["John", "johnsmith@mail.com", "john00@mail.com"],
                ["Mary", "mary@mail.com"],
                ["John", "johnnybravo@mail.com"],
            ]
        )
    )
    print(
        sol.accountsMerge(
            accounts=[
                ["Gabe", "Gabe0@m.co", "Gabe3@m.co", "Gabe1@m.co"],
                ["Kevin", "Kevin3@m.co", "Kevin5@m.co", "Kevin0@m.co"],
                ["Ethan", "Ethan5@m.co", "Ethan4@m.co", "Ethan0@m.co"],
                ["Hanzo", "Hanzo3@m.co", "Hanzo1@m.co", "Hanzo0@m.co"],
                ["Fern", "Fern5@m.co", "Fern1@m.co", "Fern0@m.co"],
            ]
        )
    )
    print(
        sol.accountsMerge(
            accounts=[
                ["Alex", "Alex5@m.co", "Alex4@m.co", "Alex0@m.co"],
                ["Ethan", "Ethan3@m.co", "Ethan3@m.co", "Ethan0@m.co"],
                ["Kevin", "Kevin4@m.co", "Kevin2@m.co", "Kevin2@m.co"],
                ["Gabe", "Gabe0@m.co", "Gabe3@m.co", "Gabe2@m.co"],
                ["Gabe", "Gabe3@m.co", "Gabe4@m.co", "Gabe2@m.co"],
            ]
        )
    )


if __name__ == "__main__":
    test()
