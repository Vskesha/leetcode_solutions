def is_isomorphic(s: str, t: str) -> bool:
    mp = {}
    for i in range(len(s)):
        a = s[i]
        b = t[i]
        if a not in mp:
            if b not in mp.values():
                mp[a] = b
            else:
                return False
        elif mp[a] != b:
            return False
    return True


if __name__ == '__main__':
    print(is_isomorphic('badc', 'baba'))
    print(bool([0] * 100))
