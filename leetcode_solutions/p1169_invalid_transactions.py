from collections import defaultdict


class Solution:
    def invalidTransactions(self, transactions: list[str]) -> list[str]:
        res = []

        aux = defaultdict(list)
        for ta in transactions:
            tal = ta.split(',')
            tal[1] = int(tal[1])
            tal[2] = int(tal[2])
            aux[tal[0]].append(tal[1:])

        for name, tals in aux.items():
            for i, tal in enumerate(tals):
                if tal[1] > 1000:
                    res.append(f'{name},{tal[0]},{tal[1]},{tal[2]}')
                    continue
                for j, tal2 in enumerate(tals):
                    if i == j:
                        continue
                    if tal[2] != tal2[2] and abs(tal[0] - tal2[0]) <= 60:
                        res.append(f'{name},{tal[0]},{tal[1]},{tal[2]}')
                        break

        return res


class Solution2:
    def invalidTransactions(self, transactions: list[str]) -> list[str]:
        res = []
        n = len(transactions)
        for i in range(n):
            ta = transactions[i]
            tal = ta.split(',')
            if int(tal[2]) > 1000:
                res.append(ta)
                continue
            for j in range(n):
                if i == j:
                    continue
                ta2 = transactions[j]
                tal2 = ta2.split(',')
                if tal2[0] == tal[0]:
                    if tal2[3] != tal[3]:
                        if abs(int(tal2[1]) - int(tal[1])) <= 60:
                            res.append(ta)
                            break
        return res


def main():
    sol = Solution()
    print(' ["alice,20,800,mtv", "alice,50,100,beijing"]\n', sol.invalidTransactions(transactions=["alice,20,800,mtv", "alice,50,100,beijing"]))
    print(' ["alice,50,1200,mtv"]\n', sol.invalidTransactions(transactions=["alice,20,800,mtv", "alice,50,1200,mtv"]))
    print(' ["bob,50,1200,mtv"]\n', sol.invalidTransactions(transactions=["alice,20,800,mtv", "bob,50,1200,mtv"]))
    print(' ["alice,20,800,mtv", "alice,50,100,mtv", "alice,51,100,frankfurt"]\n', sol.invalidTransactions(["alice,20,800,mtv", "alice,50,100,mtv", "alice,51,100,frankfurt"]))


if __name__ == '__main__':
    main()
