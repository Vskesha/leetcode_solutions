import time


def num_similar_groups(strs):
    def are_similar(s1: str, s2: str) -> bool:
        diffs = 0
        for a, b in zip(s1, s2):
            if a != b:
                diffs += 1
                if diffs > 2:
                    return False
        return True

    def dfs(el):
        visited[el] = False
        for node in similar[el]:
            if visited[node]:
                dfs(node)

    ls = len(strs)
    similar = [[] for _ in range(ls)]
    for i in range(ls):
        for j in range(i + 1, ls):
            if are_similar(strs[i], strs[j]):
                similar[i].append(j)
                similar[j].append(i)

    groups = 0
    visited = [True] * ls
    for i in range(ls):
        if visited[i]:
            dfs(i)
            groups += 1

    return groups


if __name__ == '__main__':
    t1 = time.perf_counter_ns()
    print('2 ===', num_similar_groups(["tars", "rats", "arts", "tras", "star"]))  # tras
    print('1 ===', num_similar_groups(["omv", "ovm"]))
    print('5 ===',
          num_similar_groups(["kccomwcgcs", "socgcmcwkc", "sgckwcmcoc", "coswcmcgkc", "cowkccmsgc",
                              "cosgmccwkc", "sgmkwcccoc", "coswmccgkc", "kowcccmsgc", "kgcomwcccs"]))
    print('11 ===', num_similar_groups(["qihcochwmglyiggvsqqfgjjxu","gcgqxiysqfqugmjgwclhjhovi","gjhoggxvcqlcsyifmqgqujwhi","wqoijxciuqlyghcvjhgsqfmgg","qshcoghwmglygqgviiqfjcjxu","jgcxqfqhuyimjglgihvcqsgow","qshcoghwmggylqgviiqfjcjxu","wcoijxqiuqlyghcvjhgsqgmgf","qshcoghwmglyiqgvigqfjcjxu","qgsjggjuiyihlqcxfovchqmwg","wcoijxjiuqlyghcvqhgsqgmgf","sijgumvhqwqioclcggxgyhfjq","lhogcgfqqihjuqsyicxgwmvgj","ijhoggxvcqlcsygfmqgqujwhi","qshcojhwmglyiqgvigqfgcjxu","wcoijxqiuqlyghcvjhgsqfmgg","qshcojhwmglyiggviqqfgcjxu","lhogcgqqfihjuqsyicxgwmvgj","xscjjyfiuglqigmgqwqghcvho","lhggcgfqqihjuqsyicxgwmvoj","lhgocgfqqihjuqsyicxgwmvgj","qihcojhwmglyiggvsqqfgcjxu","ojjycmqshgglwicfqguxvihgq","sijvumghqwqioclcggxgyhfjq","gglhhifwvqgqcoyumcgjjisqx"]))
    print(f'result in {time.perf_counter_ns() - t1}')