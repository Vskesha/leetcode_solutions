import test
from collections import defaultdict


def length_of_longest_substring_without_repeating(s: str) -> int:
    chars = defaultdict(int)
    begin = end = maxlen = 0
    while end < len(s):
        char = s[end]
        chars[char] += 1
        while chars[char] > 1:
            chars[s[begin]] -= 1
            begin += 1
        end += 1
        lenght = end - begin
        if maxlen < lenght:
            maxlen = lenght
    return maxlen


def length_of_longest_substring_without_repeating2(s: str) -> int:
    # make map for the letters
    alphabet = {}
    # make ans var
    ans = 0
    # get len of input
    n = len(s)
    # make start ptr will be where non repeating substring starts
    start = 0

    # enumerate input
    for index, letter in enumerate(s):
        # if curr char in map
        if letter in alphabet:
            # get val of char in map (that char index) + 1 and store in sums var
            # so sums is next index
            sums = alphabet[letter] + 1

            # if sums var > start
            if sums > start:
                # update start, because start will be be where ans begins
                start = sums

        # make num var set to index - start + 1
        # getting len here
        num = index - start + 1

        # if num(aka the len) > ans
        if num > ans:
            # update ans
            ans = num

        # put letter in map with index as val
        alphabet[letter] = index

    # return ans
    return ans


if __name__ == '__main__':
    test.assert_equals(length_of_longest_substring_without_repeating("abcabcbb"), 3)
    test.assert_equals(length_of_longest_substring_without_repeating("bbbbb"), 1)
    test.assert_equals(length_of_longest_substring_without_repeating("pwwkew"), 3)

    test.assert_equals(length_of_longest_substring_without_repeating2("abcabcbb"), 3)
    test.assert_equals(length_of_longest_substring_without_repeating2("bbbbb"), 1)
    test.assert_equals(length_of_longest_substring_without_repeating2("pwwkew"), 3)
