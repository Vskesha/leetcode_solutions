import re


def main():
    inp = input('Type title of the problem: ')
    filename = 'p' + re.sub(r'[^a-zA-Z0-9]+', '_', inp.lower().strip().replace("'", "")) + '.py'

    with open(filename, 'x') as f:
        pass


if __name__ == '__main__':
    main()
