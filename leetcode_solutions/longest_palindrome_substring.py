def longest_palindrome_substring(s: str) -> str:

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


if __name__ == '__main__':
    print(longest_palindrome_substring("aacabdkacaa"))
