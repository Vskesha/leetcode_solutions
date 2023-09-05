def longest_common_prefix(strs: list[str]) -> str:
    ans = 0
    for letters in zip(*strs):
        if len(set(letters)) == 1:
            ans += 1
        else:
            break
    return strs[0][:ans]


def longest_common_prefix2(strs: list[str]) -> str:

    def char_in_all_strings(i: int) -> bool:
        char = strs[0][i]
        for s in strs:
            if s[i] != char:
                return False
        return True

    min_len_str = min(strs, key=len)
    min_len = len(min_len_str)
    for i in range(min_len):
        if not char_in_all_strings(i):
            return strs[0][:i]

    return min_len_str


if __name__ == '__main__':
    print(longest_common_prefix(["flower", "flow", "flight"]))
    print(longest_common_prefix(["dog", "racecar", "car"]))
    print(longest_common_prefix(['vsk', 'vske', 'vskesha']))
    print(longest_common_prefix(["cir", "car"]))
