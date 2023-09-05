def convert_to_title(column_number: int) -> str:
    res = ''
    while column_number > 0:
        ch = chr((column_number - 1) % 26 + 65)
        res = ch + res
        column_number = (column_number - 1) // 26
    return res


def title_to_number(column_title: str) -> int:
    res = 0
    for ch in column_title:
        res = res * 26 + ord(ch) - 64
    return res


if __name__ == '__main__':
    print('vs')
    for i in range(1, 100):
        st = convert_to_title(i)
        n = title_to_number(st)
        print(st, n)
