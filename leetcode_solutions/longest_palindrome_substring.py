import time


def longest_palindrome_substring1(s: str) -> str:

    def is_palindrome(left_index, right_index):
        while left_index < right_index:
            if s[left_index] != s[right_index]:
                return False
            left_index += 1
            right_index -= 1
        return True

    max_len = 0
    start = 0
    left = 0
    while left < len(s) - max_len:
        for right in range(len(s), left+max_len, -1):
            if is_palindrome(left, right-1):
                start = left
                max_len = right - left
                break
        left += 1
    return s[start:start+max_len]


def longest_palindrome_substring2(s: str) -> str:
    if not s:
        return ''
    max_len = 0
    start = 0
    ln = len(s)
    for i in range(ln):
        for a in range(2):
            left, right = i, i + a
            while left >= 0 and right < ln and s[left] == s[right]:
                left -= 1
                right += 1
            if max_len < right - left - 1:
                max_len = right - left - 1
                start = left + 1
    return s[start:start+max_len]


if __name__ == '__main__':
    for func in (longest_palindrome_substring1, longest_palindrome_substring2):
        t1 = time.perf_counter()
        for _ in range(1000):
            func("aacabdkacaa")
        t2 = time.perf_counter()
        print(f'{func.__name__} returns "{func("aacabdkacaa")}" 1000 times in {t2-t1:.03f} sec')
