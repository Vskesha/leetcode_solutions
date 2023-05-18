def count_and_say(n: int):
    ans = '1'
    for _ in range(n-1):
        res = ''
        counter = 0
        char = ans[0]
        for c in ans:
            if c == char:
                counter += 1
            else:
                res += f'{counter}{char}'
                counter = 1
                char = c
        ans = res + f'{counter}{char}'
    return ans
        

if __name__ == '__main__':
    print('1 ===', count_and_say(1))
    print('1211 ===', count_and_say(4))