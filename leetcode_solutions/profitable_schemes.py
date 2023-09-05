from itertools import combinations


def profitableSchemes(n: int, minProfit: int, group: list[int], profit: list[int]) -> int:
    total = 0
    l = len(group)
    for k in range(l + 1):
        for comb in combinations(range(l), k):
            people = sum(group[i] for i in comb)
            if people > n:
                continue
            curr_profit = sum(profit[i] for i in comb)
            if curr_profit >= minProfit:
                total += 1
    return total


if __name__ == '__main__':
    print('2 ====', profitableSchemes(n=5, minProfit=3, group=[2, 2], profit=[2, 3]))
    print('7 ====', profitableSchemes(n=10, minProfit=5, group=[2, 3, 5], profit=[6, 7, 8]))
    print('2 ====', profitableSchemes(n=64, minProfit=0, group=[80, 40], profit=[88, 88]))
