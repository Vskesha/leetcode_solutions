def max_vowels(s: str, k: int) -> int:
    vowels = {'a', 'e', 'i', 'o', 'u'}
    max_count = sum(1 for c in s[:k] if c in vowels)
    tmp = max_count
    for a, b in zip(s, s[k:]):
        if a in vowels:
            tmp -= 1
        if b in vowels:
            tmp += 1
        if tmp == k:
            return k
        if max_count < tmp:
            max_count = tmp
    return max_count


def max_vowels2(s: str, k: int) -> int:
    vowels = {'a', 'e', 'i', 'o', 'u'}
    is_vowels = [c in vowels for c in s]
    max_count = count = sum(map(int, is_vowels[:k]))
    for i in range(len(s) - k):
        if not is_vowels[i] and is_vowels[i + k]:
            count += 1
            if max_count < count:
                if count == k:
                    return k
                max_count = count
        elif is_vowels[i] and not is_vowels[i + k]:
            count -= 1
    return max_count


if __name__ == '__main__':
    print('3 ===', max_vowels('abciiidef', 3))
    print('2 ===', max_vowels('aeiou', 2))
    print('2 ===', max_vowels('leetcode', 3))
    print('1 ===', max_vowels('tryhard', 4))
